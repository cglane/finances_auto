import json
import pygsheets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework.views import APIView

from finances.machine_learning import PredictionModel
from finances.models import Transaction
from finances.serializers import TransactionSerializer
from finances.lib.preAmex import  amexCSV
from finances.lib.preCapitolOne import CapitolOneCSV
from finances.lib.preBOA import BOACSV

class MainView(TemplateView):
    template_name = "base.html"

def serialize_dict(obj):
    serializer = TransactionSerializer(data=obj)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)

@csrf_exempt
def authorize(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        gc = pygsheets.authorize()
        return JsonResponse({'sucess': True}, status=200)

    return JsonResponse( status=400)

@csrf_exempt
def sheets_list(request):
    gc = pygsheets.authorize()
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        sheets = gc.list_ssheets()
        return JsonResponse(sheets, safe=False)

    return JsonResponse( status=400)

class ReadCSV(APIView):
    """Receive list of csv lines from browser and parse
        based on the credit card company
    """
    pred = PredictionModel()
    pred.train_descriptions()
    pred.train_source()

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        if data['type']:
            if data['type'] == 'AMEX':
                fileParser = amexCSV(data['csvList'])
                dict_list = fileParser.readFile()
            elif data['type'] == 'CapitolOne':
                fileParser = CapitolOneCSV(data['csvList'])
                dict_list = fileParser.readFile()
            elif data['type'] == 'BOA':
                fileParser = BOACSV(data['csvList'])
                dict_list = fileParser.readFile()
            try:
                print 'finished training'
                keys, rows = self.pred.describe_transactions(dict_list)
                return JsonResponse({'keys':keys, 'rows': rows}, status=200, safe=False)
            except ValueError as e:
                print e
                return JsonResponse({'success': 'false', 'msg': str(e)}, status=400)
            # return JsonResponse(dict_list, status=200, safe=False)
        return JsonResponse({'success': 'false', 'msg': 'wrong type'}, status=400)

class UpdateData(APIView):
    def post(self, request):
        """Receive a rows from data table and add to new google sheet & add to DB"""

        gc = pygsheets.authorize()
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        if isinstance(data['tableRows'], list):
            spread_sheet = gc.create(data['title'])
            wks = spread_sheet[0]
            for row in data['tableRows']:
                data_dict = dict(zip(data['tableKeys'], row))
                exists_db = Transaction.objects.filter(
                    date=data_dict.get('date'),
                    amount=data_dict.get('amount'),
                    location=data_dict.get('location')
                )
                if not exists_db:
                    wks.append_table(values=row)
                    transaction = Transaction(**data_dict)
                    transaction.save()
            return JsonResponse({'success': 'true'}, status=200)
        return JsonResponse({'success': 'false'}, status=400)

    def put(self, request):
        """Receive a rows from data table and add to existing google sheet & add to DB"""

        gc = pygsheets.authorize()
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        if isinstance(data['tableRows'], list):
            spread_sheet = gc.open(data['title'])
            wks = spread_sheet[0]
            for row in data['tableRows']:
                data_dict = dict(zip(data['tableKeys'], row))
                exists_db = Transaction.objects.filter(
                    date=data_dict.get('date'),
                    amount=data_dict.get('amount'),
                    location=data_dict.get('location')
                )
                if not exists_db:
                    wks.append_table(values=row)
                    transaction = Transaction(**data_dict)
                    transaction.save()
            return JsonResponse({'success': 'true'}, status=200)
        return JsonResponse({'success': 'false'}, status=400)


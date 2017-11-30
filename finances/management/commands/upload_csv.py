import pygsheets
from django.core.management.base import BaseCommand, CommandError
from finances.models import Transaction
import datetime
gc = pygsheets.authorize()


def getRowDict(row):
    rtrn_dict = {}
    date = row[0]

    d = datetime.datetime.strptime(date, '%m/%d/%Y')
    formatted_date = datetime.date.strftime(d, "%Y-%m-%d")

    rtrn_dict['date'] = formatted_date
    ##Amounts are different columns
    amount_spaces = row[1:4]
    source = "Salary"
    if row[1]:
        source = "Salary"
    elif row[2]:
        source = "Amount BankSC"
    elif row[3]:
        source = "13 Drews Ct."
    elif row[4]:
        source = "Work Related"
    rtrn_dict['source'] = source
    if any(amount_spaces):
        rtrn_dict['amount'] = next(s for s in amount_spaces if s)
    rtrn_dict['description'] = row[5]
    rtrn_dict['location'] = row[6]
    return rtrn_dict

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Open spreadsheet and then workseet
        sh = gc.open('Finances')
        wks = sh[0]
        for itr, row in enumerate(list(wks)[1:]):
            print ('Curr Row : ', itr)
            row_dict = getRowDict(row)
            if row_dict.get('amount'):
                try:
                    query = Transaction.objects.filter(date=row_dict['date'], amount=row_dict['amount'],
                                                       description=row_dict['description'])
                    print query[0].source                                                
                    if not query:
                        transaction = Transaction.objects.create(**row_dict)
                        print ('Added: ', itr)
                    else:
                        query.update(source=row_dict['source'])
                        print ('Already Added: ', itr)
                except ValueError as e:
                    print e
                    print ('Row #: ', itr)
            else:
                print ('No Amount Value: ', itr)
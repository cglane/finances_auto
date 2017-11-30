from django.core.management.base import BaseCommand, CommandError
from finances.models import Transaction
import pygsheets
import pandas as pd
import time

class Command(BaseCommand):
    def addSheet(self, df):
        sheet_name="Finances2.0"
        gc = pygsheets.authorize()
        spread_sheet = gc.open(sheet_name)
        wks = spread_sheet[0]
        ##Drop the .0 from float as it is done automatically iin Sheets and
        ##needs to be dropped for comparison reasons

        wks_string_list = [
            str(" ".join([x[0], 
            '{0:g}'.format(float(x[1]))
            ])
        ) for x in list(wks)[1:]]
        print wks_string_list[0:20]
        for row in df.values:
            try:
                my_row = [str(x) for x in list(row)]
                query_str = " ".join([
                    my_row[0], 
                    '{0:g}'.format(float(my_row[1]))
                ])
                print query_str
                if str(query_str) in wks_string_list:
                    print ('is in there')
                else:
                    wks.append_table(values=list(row))
                    print (' added')
                    pass
            except:
                print (row, 'fail')

    def handle(self, *args, **options):
        headers = ['date', 'amount', 'location', 'description', 'source']
        df = pd.DataFrame(
            list(
                Transaction.objects.filter(location__isnull=False, description__isnull=False).values()
            )
        )     
        df['date']  = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
        df = df[headers]
        try: 
            self.addSheet(df)
        except ValueError as e:
            print 'error'
            time.sleep(200)
            self.handle()


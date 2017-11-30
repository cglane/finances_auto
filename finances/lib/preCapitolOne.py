from collections import OrderedDict
import datetime

class CapitolOneCSV(object):
    def __init__(self, csvList):
        self.csvList = csvList

    ###Row 7 is for credits but 6 for debits
    def getValue(self,row):
        if row[6]:
            return float(row[6]) * -1
        elif row[7]:
            return float(row[7])

    def readFile(self):
        rtrn_list = []
        if isinstance(self.csvList, list):
                ###Ignore First Column and reverse list
                for row in self.csvList[1:][::-1]:
                    ###Don't want to include credit card payments
                    if any(row):
                        if ("CAPITAL ONE ONLINE" not in row[4]):
                            date = row[1]
                            d = datetime.datetime.strptime(date, '%m/%d/%Y')
                            date = datetime.date.strftime(d, "%Y-%m-%d")

                            value = self.getValue(row)
                            location = row[4]
                            rtrn_list.append(
                                OrderedDict(
                                    zip(
                                        ('date', 'amount','location'),
                                        (date,value,location)
                                    )
                                )
                            )
                return rtrn_list
        else:
            return 'CSV list not formatted correctly for CapitolOne Parser'

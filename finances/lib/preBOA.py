import datetime
from collections import OrderedDict
from csv import reader

class BOACSV(object):
    def __init__(self, csvLines):
        self.csvLines = csvLines
    def splitRow(self, rowList):
        if any(rowList):
            ###Remove Day from date string
            date = rowList[0]
            d = datetime.datetime.strptime(date, '%m/%d/%Y')
            date = datetime.date.strftime(d, "%Y-%m-%d")
            ##Adding negative sign to value
            amount =  rowList[2]
            ##Get first three fields, typically very long
            location = rowList[1]
            ##Don't want to include credit card payment data
            if 'AMERICAN EXPRESS' not in location and 'CAPITAL ONE' not in location:
                return OrderedDict(zip(('date', 'amount', 'location'),(date, amount, location)))

    def readFile(self):
        fileList = []
        if isinstance(self.csvLines, list):
            ##Need to skipp meta data
            for row in reader(self.csvLines[8:]):
                formattedRow = self.splitRow(row)
                if formattedRow:
                    fileList.append(formattedRow)
            ###Return the list backwards so it it ends with most recent purchases
            return fileList
        else:
            print "Doc must be a list"
            return []

import datetime
from collections import OrderedDict

class amexCSV(object):
    def __init__(self, csvLines):
        self.csvLines = csvLines
    def getValue(self, rowList):
        value = 0
        if rowList[9]:
            value = rowList[9]
        elif rowList[8]:
            value = rowList[8]
        elif rowList[7]:
            value = rowList[7]
        return float(value) * -1
    def splitRow(self, row):
        rowList = row.split(',')
        if any(rowList):
            ###Remove Day from date string
            date = rowList[0].split('  ')[0]
            d = datetime.datetime.strptime(date, '%m/%d/%Y')
            date = datetime.date.strftime(d, "%Y-%m-%d")
            ##Adding negative sign to value
            amount =  self.getValue(rowList)
            ##Get third item, only text before '-' and not including the "
            location = rowList[2].split(' -')[0][1:]
            if 'ONLINE PAYMENT' not in location:
                return OrderedDict(zip(('date', 'amount', 'location'),(date, amount, location)))

    def readFile(self):
        fileList = []
        if isinstance(self.csvLines, list):
            ##Reverse Order to have oldest transactions first
            for row in self.csvLines:
                formattedRow = self.splitRow(row)
                if formattedRow:
                    fileList.append(formattedRow)
            ###Return the list backwards so it it ends with most recent purchases
            return fileList
        else:
            print "Doc must be a list"
            return []

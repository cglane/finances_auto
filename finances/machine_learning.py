from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
import pandas as pd
from scipy.sparse import coo_matrix, hstack
import numpy as np
# from training.lib import preAmex, preCapitolOne, preFinances
from finances.models import Transaction

class PredictionModel(object):
    def __init__(self, userId=1):
        self.df = pd.DataFrame(
            list(
                Transaction.objects.filter(location__isnull=False, description__isnull=False).values()
            )
        )

    def train_data(self):
        self.vectorizer = CountVectorizer()
        ##Train Vectorizer
        location_list = self.df['location'].tolist()
        location_list = self.vectorizer.fit_transform(location_list).toarray().tolist()
        ##Add amount to vectors
        amount_list  = self.df['amount'].tolist()
        train_list = [list(x) + [amount_list[itr]] for itr, x in enumerate(location_list)]
        ##Initialize Linear SVC
        self.clf = svm.LinearSVC(random_state=0)
        print 'fitting'
        self.clf.fit(train_list, self.df['description'])
        print 'done fitting'
        return self.vectorizer, self.clf

    def describe_transactions(self, transactions):
        """"Expecting transaction to be in format
            {date: '', amount: '', location: '', description: '', source: ''}
        """
        rtrnList = []
        for item in transactions:
            item_found = Transaction.objects.filter(
                date=item['date'],
                location=item['location'],
                amount=item['amount']
            )
            if not item_found:
                ##Vectorize location
                location_list = self.vectorizer.transform([item['location']]).toarray().tolist()[0]
                ##Add Amount to vector
                location_list.append(float(item['amount']))
                ##Predict based on Vector + amount
                description = self.clf.predict([location_list])[0]
                item.update({'description': description})
                item.update({'source': 'Salary'})
                rtrnList.append(item)
        keys = rtrnList[0].keys()
        rows = [x.values() for x in rtrnList]
        print rows
        return keys , rows
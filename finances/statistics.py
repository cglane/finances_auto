from finances.models import Transaction
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
sns.set_style('whitegrid')
class StatsClass(object):
    keywords = {
        'alcohol' : ['alcohol', 'beer', 'bar'],
        'restaurant': ['restaurant', 'meal'],
        'groceries': ['groceries'],
        'taxes': ['taxes'],
        'car': ['car', 'parking','gasoline', 'gas']
    }
    def __init__(self):
         self.df = pd.DataFrame(
            list(
                Transaction.objects.filter(location__isnull=False, description__isnull=False).values()
            )
        )     
    def amountDescription(self, description):     
        if self.keywords.get(description):
            keywords = self.keywords.get(description)
            keyword_query = "|".join(keywords)
        else:
            keyword_query = description
        filtered_df = self.df[self.df['description'].str.contains(keyword_query, case=False)]
        filtered_df['date'] = pd.to_datetime(filtered_df['date'], errors='coerce')
        print filtered_df.groupby(filtered_df['date'].map(lambda x: x.year)).head()

        # filtered_df = filtered_df.set_index('date')
        # filtered_df = filtered_df.groupby([pd.TimeGrouper('M'),'description']).sum()
        # filtered_df.loc['Total']  = pd.Series(filtered_df['amount'].sum(), index = ['amount'])

   
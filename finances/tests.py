from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from finances.models import Transaction

class SheetsTest(APITestCase):
    # def test_authorize(self):
    #     """
    #     Ensure we can create a new account object.
    #     """
    #     url = reverse('authorize')
    #     print (url, 'url')
    #     data = {'name': 'DabApps'}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, 200)
    # def test_get_sheets(self):
    #     """
    #     Ensure we can create a new account object.
    #     """
    #     url = reverse('sheets_list')
    #     print (url, 'url')
    #     data = {'name': 'DabApps'}
    #     response = self.client.get(url, data, format='json')
    #     print response
    #     self.assertEqual(response.status_code, 200)

    # def test_update_sheet(self):
    #     """
    #     Ensure we can create a new account object.
    #     """
    #     url = '/api/v1/add_data/'
    #     data = {'title': "Test Spreadsheet",
    #             'map':['date', 'location', 'amount', 'description'],
    #             'dataTable': [['2017-10-10','here' ,'-10.5', 'there']]
    #             }
    #     response = self.client.put(url, data, format='json')
    #     self.assertEqual(response.status_code, 200)
    # def test_create_sheet(self):
        # """
        # Ensure we can create a new account object.
        # """
        # url = '/api/v1/add_data/'
        # data = {'title': "Untitled spreadsheet",
        #         'map':['date', 'location', 'amount', 'description'],
        #         'dataTable': [['2017-10-10','here' ,'-10.5', 'there']]
        #         }
        # response = self.client.post(url, data, format='json')
        # print response
        # self.assertEqual(response.status_code, 200)
    def test_describe_transactions(self):
        transactions = [
            {'date': '2017-10-10', 'location': 'BiLo', 'amount': '-3.0'}
        ]
        url = '/api/v1/describe_transactions'
        print url
        response = self.client.post(url, {"transactions": transactions}, format='json')
        print response
        self.assertEqual(response.status_code, 200)
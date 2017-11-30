from django.core.management.base import BaseCommand, CommandError
import requests

class Command(BaseCommand):
    def handle(self, *args, **options):
        transactions = [
            {'date': '2017-10-10', 'location': 'BiLo', 'amount': '-3.0'}
        ]
        url = 'http://localhost:8000/api/v1/describe_transactions'
        print url
        response = requests.post(url)

        print response

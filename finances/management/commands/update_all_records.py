from django.core.management.base import BaseCommand, CommandError
from finances.models import Transaction

class Command(BaseCommand):
    def handle(self, *args, **options):
        transactions = Transaction.objects.filter()
        transactions.update(user=2)
        

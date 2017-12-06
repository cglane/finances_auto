from django.core.management.base import BaseCommand, CommandError
from finances.models import Transaction
from finances.statistics import StatsClass

class Command(BaseCommand):
    def handle(self, *args, **options):
        stats = StatsClass()
        stats.amountDescription('car')
        

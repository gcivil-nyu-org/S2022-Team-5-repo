import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from Property.models import ChartsManhattan


class Command(BaseCommand):
    help = 'Load data from CO2 file'

    def handle(self, *args, **kwargs):
        datafile1 = settings.BASE_DIR / 'data' / 'Manhattan_2021_a.csv'
        with open(datafile1, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                x = row['SALE PRICE']
                y = ''.join(map(str, x))
                z = int(y)
                ChartsManhattan.objects.get_or_create(neighbourhood=row['NEIGHBORHOOD'], price=z)

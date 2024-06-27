import pandas as pd
from models import CsvData
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import data from CSV to SQLite database'

    def handle(self, *args, **kwargs):
        file_path = 'static/data.csv'
        df = pd.read_csv(file_path)

        for index, row in df.iterrows():
            CsvData.objects.create(
                time=int(row['time']),
                max_current=int(row['max_current']),
                avg_current=int(row['avg_current']),
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
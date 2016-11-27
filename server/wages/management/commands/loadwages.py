from django.core.management.base import BaseCommand, CommandError
from wages.models import Wage, Title, Department, Agency
import pandas as pd


class Command(BaseCommand):
    help = 'Loads wage data from a csv'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='+', type=str)

    def handle(self, *args, **options):
        for input_file in options['csv_path']:
            df = pd.read_csv(input_file)
            entries = []
            for i, row in df.iterrows():
                agency, _ = Agency.objects.get_or_create(name=row['AGENCY'])
                dept, _ = Department.objects.get_or_create(name=row['DEPT'])
                title, _ = Title.objects.get_or_create(name=row['TITLE'])
                first_name = row['FIRST_NAME']
                middle_name = row['MIDDLE_NAME']
                last_name = row['LAST_NAME']
                wage = round(row['WAGES'], 2)
                year = row['YEAR']

                new_instance, _ = Wage.objects.get_or_create(
                    first_name=row['FIRST_NAME'],
                    middle_name=row['MIDDLE_NAME'],
                    last_name=row['LAST_NAME'],
                    agency=agency,
                    dept=dept,
                    title=title,
                    wage=round(row['WAGES'], 2),
                    year=row['YEAR']
                )
                new_instance.save()
        self.stdout.write('Wages loaded')

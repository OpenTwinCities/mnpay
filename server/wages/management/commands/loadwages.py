from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from wages.models import Wage, Title, Department, Government, Agency
import pandas as pd
from collections import defaultdict


object_buff = defaultdict(dict)

def buffered_get_or_create(cls, name):
    if name not in object_buff[cls.__name__]:
        object_buff[cls.__name__][name] = cls.objects.create(name=name)
    return object_buff[cls.__name__][name]


class Command(BaseCommand):
    help = 'Loads wage data from a csv'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='+', type=str)

    def handle(self, *args, **options):
        for input_file in options['csv_path']:
            df = pd.read_csv(input_file)
            df.fillna("")
            entries = []
            for i, row in df.iterrows():
                if i % 1000 == 0:
                    self.stdout.write("{0}/{1}".format(i, len(df)))
                gov, _ = Government.objects.get_or_create(
                             name=row['GOVERNMENT']
                         )
                agency = buffered_get_or_create(Agency, row['AGENCY'])
                dept = buffered_get_or_create(Department, row['DEPT'])
                title = buffered_get_or_create(Title, row['TITLE'])
                first_name = row['FIRST_NAME']
                middle_name = row['MIDDLE_NAME']
                last_name = row['LAST_NAME']
                wage = round(row['WAGES'], 2)
                year = row['YEAR']

                if wage > 0:
                    entries.append(
                        Wage(
                            first_name=row['FIRST_NAME'],
                            middle_name=row['MIDDLE_NAME'],
                            last_name=row['LAST_NAME'],
                            government=gov,
                            agency=agency,
                            dept=dept,
                            title=title,
                            wage=round(row['WAGES'], 2),
                            year=row['YEAR']
                        )
                    )
                if i % 100000 == 0:
                    Wage.objects.bulk_create(entries)
                    entries = []
            Wage.objects.bulk_create(entries)
        self.stdout.write('Wages loaded')

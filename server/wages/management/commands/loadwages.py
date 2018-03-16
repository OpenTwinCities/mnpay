from collections import defaultdict

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from wages import models
from . import extractors


object_buff = defaultdict(dict)

def buffered_get_or_create(cls, name):
    if name not in object_buff[cls.__name__]:
        object_buff[cls.__name__][name] = cls.objects.create(name=name)
    return object_buff[cls.__name__][name]


def clear_entries():
    models.Wage.objects.all().delete()
    models.Government.objects.all().delete()
    models.Agency.objects.all().delete()
    models.Department.objects.all().delete()
    models.Title.objects.all().delete()


class Command(BaseCommand):
    help = 'Loads wage data.'

    def add_arguments(self, parser):
        parser.add_argument('resource_path', type=str)

    def handle(self, *args, **options):
        resource_path = options['resource_path']
        clear_entries()


        entries = []
        records = set(extractors.load_all(resource_path))
        for i, row in enumerate(records):
            if i % 1000 == 0:
                self.stdout.write("{0}/{1}".format(i, len(records)))
            gov = buffered_get_or_create(models.Government, row.government)
            agency = buffered_get_or_create(models.Agency, row.agency)
            dept = buffered_get_or_create(models.Department, row.dept)
            title = buffered_get_or_create(models.Title, row.title)
            first_name = row.first_name
            middle_name = row.middle_name
            last_name = row.last_name
            wage = round(row.wage, 2)
            year = row.year

            if wage > 0:
                entries.append(
                    models.Wage(
                        first_name=first_name,
                        middle_name=middle_name,
                        last_name=last_name,
                        government=gov,
                        agency=agency,
                        dept=dept,
                        title=title,
                        wage=wage,
                        year=year
                    )
                )
        models.Wage.objects.bulk_create(entries)
        self.stdout.write('Wages loaded')

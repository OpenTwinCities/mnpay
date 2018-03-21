from collections import defaultdict

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from wages import models
from . import extractors


def bulk_create_supporting(data):
    supporting_models = {
        models.Government: 'government',
        models.Agency: 'agency',
        models.Department: 'dept',
        models.Title: 'title'
    }
    records = {}
    for sup_model, field in supporting_models.items():
        names = {
            getattr(item, field)
            for item in data
            if getattr(item, field) is not None
        }
        model_instances = [sup_model(name=name) for name in names]
        sup_model.objects.bulk_create(model_instances)
        created = sup_model.objects.all()
        records[sup_model.__name__] = {item.name: item for item in created}
    return records


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
        buffered_models = bulk_create_supporting(records)
        for i, row in enumerate(records):
            if i % 1000 == 0:
                self.stdout.write("{0}/{1}".format(i, len(records)))
            gov = buffered_models[models.Government.__name__][row.government]
            agency = buffered_models[models.Agency.__name__][row.agency]
            dept = buffered_models[models.Department.__name__][row.dept]
            title = buffered_models[models.Title.__name__][row.title]
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

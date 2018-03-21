import csv

from . import utils


def etl(path, year):
    with open(path) as f:
        reader = csv.DictReader(f)
        return [_transform_row(row, year) for row in reader]

def _transform_row(raw_row, year):
    last, first_middle = raw_row['Name'].split(',', 1)
    first, *possible_middle = first_middle.rsplit(' ', 1)
    middle = possible_middle[0] if len(possible_middle) > 0 else ''
    return utils.Wage(**{
        'first_name': first if first else '',
        'last_name': last if last else '',
        'middle_name': middle if middle else '',
        'government': 'Minneapolis',
        'agency': 'Minneapolis Park Board',
        'dept': raw_row['Location Description'],
        'title': raw_row['Job Title'],
        'wage': float(raw_row['Annual Rt']),
        'year': year
    })

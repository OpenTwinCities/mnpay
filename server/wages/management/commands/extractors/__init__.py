import os

from . import minneapolis_park_board
from . import migrated


def _load_minneapolis_park_board(resource_path):
    results = []
    path = os.path.join(resource_path, 'minneapolis_park_board')
    for year in range(2007, 2018):
        filename = '{0}.csv'.format(year)
        full_path = os.path.join(path, filename)
        results.extend(minneapolis_park_board.etl(full_path, year))
    return results


def _load_migrated(resource_path):
    results = []
    path = os.path.join(resource_path, 'migrated')
    for file_number in range(1, 19):
        filename = 'file_{0}.json'.format(file_number)
        full_path = os.path.join(path, filename)
        results.extend(migrated.etl(full_path))
    return results


def load_all(resource_path):
    results = []
    results.extend(_load_minneapolis_park_board(resource_path))
    results.extend(_load_migrated(resource_path))
    return list(set(results))

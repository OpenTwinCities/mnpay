import os

from . import minneapolis_park_board


def _load_minneapolis_park_board(resource_path):
    results = []
    path = os.path.join(resource_path, 'minneapolis_park_board')
    for year in range(2007, 2018):
        filename = '{0}.csv'.format(year)
        full_path = os.path.join(path, filename)
        results.extend(minneapolis_park_board.etl(full_path, year))
    return results


def load_all(resource_path):
    return _load_minneapolis_park_board(resource_path)

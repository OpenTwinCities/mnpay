import json

from . import utils


def etl(file_path):
    with open(file_path) as f:
        results = json.load(f)
    return [
        utils.Wage(
            first_name=wage['first_name'] if wage['first_name'] else '',
            last_name=wage['last_name'] if wage['last_name'] else '',
            middle_name=wage['middle_name'] if wage['middle_name'] else '',
            government=wage['government'] if wage['government'] else '',
            agency=wage['agency'] if wage['agency'] else '',
            dept=wage['dept'] if wage['dept'] else '',
            title=wage['title'] if wage['title'] else '',
            wage=float(wage['wages']),
            year=wage['year'] if wage['year'] else ''
        )
        for wage in results
    ]

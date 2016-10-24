"""load_in_csv.py

Usage:
    load_in_csv.py <input_file>
"""
from app import db, models
import pandas as pd
from docopt import docopt


def main(input_file):
    df = pd.read_csv(input_file)
    entries = []
    for i, row in df.iterrows():
        entries.append(models.Salary(
            first_name=row["FIRST_NAME"],
            middle_name=row["MIDDLE_NAME"],
            last_name=row["LAST_NAME"],
            agency=row["AGENCY"],
            dept=row["DEPT"],
            wages=round(row["WAGES"], 2),
            year=row["YEAR"],
            title=row["TITLE"]
        ))
    db.session.bulk_save_objects(entries)
    db.session.commit()


if __name__ == "__main__":
    arguments = docopt(__doc__)
    main(arguments["<input_file>"])

"""convert_pioneer_web_wages_to_csv.py

Usage:
    convert_pioneer_web_wages_to_csv.py <input_file> <output_file>
"""
from docopt import docopt
import pandas as pd


def _split_name_col(series):
    ret_df = pd.DataFrame()
    df = series.str.strip().str.split(" ", 1, expand=True).fillna(" ")

    ret_df["FIRST_NAME"] = df[0].str.title()
    ret_df["MIDDLE_NAME"] = df[1].str.title()
    return ret_df


def main(input_file, output_file):
    df = pd.read_csv(input_file, sep="|")
    name_df = _split_name_col(df["restname"])

    txt_col_interest = [
        "lastname",
        "govt",
        "agency",
        "dept",
        "title"
    ]

    non_txt_col_interest = [
        "salary",
        "datayear"
    ]

    refined = pd.DataFrame()
    for key in txt_col_interest:
        refined[key] = df[key].str.title().str.strip()

    for key in non_txt_col_interest:
        refined[key] = df[key]

    refined.columns = ["LAST_NAME",
                       "GOVERNMENT",
                       "AGENCY",
                       "DEPT",
                       "TITLE",
                       "WAGES",
                       "YEAR"]
    refined = pd.concat([name_df, refined], axis=1)
    refined.to_csv(output_file, index=False)


if __name__ == "__main__":
    arguments = docopt(__doc__)
    main(arguments["<input_file>"],
         arguments["<output_file>"])

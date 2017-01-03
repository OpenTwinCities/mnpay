"""convert_umn_wages_to_csv.py

Usage:
    convert_umn_wages_to_csv.py <input_file> <output_file>
"""
from docopt import docopt
from openpyxl import load_workbook
import pandas as pd


def _convert_ws_to_df(ws):
    data = ws.values
    cols = next(data)
    return pd.DataFrame(data, columns=cols)


def _split_name_col(series):
    ret_df = pd.DataFrame()
    df = series.str.split(",", expand=True)
    ret_df["LAST_NAME"] = df[0].str.title()
    df = df[1].str.split(" ", 1, expand=True).fillna(" ")
    ret_df["FIRST_NAME"] = df[0].str.title()
    ret_df["MIDDLE_NAME"] = df[1].str.title()
    return ret_df


def main(input_file, output_file):
    wb = load_workbook(filename=input_file)
    df = _convert_ws_to_df(wb["Sheet 1"])
    df["AGENCY"] = "University of Minnesota"
    df["WAGES"] = df["TOT_DWEO_SALARY"]
    df["DEPT"] = df["UM_COLLEGE_DESCR"].str.title()
    df["TITLE"] = df["JOBCODE_DESCR"].str.title()
    df["YEAR"] = 2016
    df = df[["LAST_NAME",
             "FIRST_NAME",
             "MIDDLE_NAME",
             "AGENCY",
             "DEPT",
             "TITLE",
             "WAGES",
             "YEAR"]]
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    arguments = docopt(__doc__)
    main(arguments["<input_file>"],
         arguments["<output_file>"])

"""convert_washington_cty_wages_to_csv.py

Usage:
    convert_washington_cty_wages_to_csv.py <input_file> <output_file>
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
    final = pd.DataFrame()
    years = [2015, 2014, 2013]
    sheet_name_tmplate = "{year} Wages"
    wb = load_workbook(filename=input_file)
    for year in years:
        df = _convert_ws_to_df(wb[sheet_name_tmplate.format(year=year)])
        df["AGENCY"] = "Washington County"
        df["WAGES"] = df["GROSS WAGES"]
        df["DEPT"] = df["DEPT"].str.title()
        df["TITLE"] = df["TITLE"].str.title()
        empl_nm = _split_name_col(df["NAME"])
        df = df[["AGENCY", "DEPT", "TITLE", "WAGES"]]
        refined = pd.concat([df, empl_nm], axis=1)
        refined["YEAR"] = year
        final = pd.concat([final, refined])
    final.to_csv(output_file, index=False)


if __name__ == "__main__":
    arguments = docopt(__doc__)
    main(arguments["<input_file>"],
         arguments["<output_file>"])

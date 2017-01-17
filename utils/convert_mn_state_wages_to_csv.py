"""convert_mn_state_wages_to_csv.py

Usage:
    convert_mn_state_wages_to_csv.py <year> <input_file> <output_file>
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
    ret_df["LAST_NAME"] = df[0]
    df = df[1].str.split(" ", 1, expand=True).fillna(" ")
    ret_df["FIRST_NAME"] = df[0]
    ret_df["MIDDLE_NAME"] = df[1]
    return ret_df


def main(input_file, output_file, year):
    wb = load_workbook(filename=input_file)
    yearpart = year[2:]
    hr_df = _convert_ws_to_df(wb["FY"+yearpart+"_HR"])
    wage_df = _convert_ws_to_df(wb["FY"+yearpart+"_EARNINGS"])
    joined = pd.merge(hr_df,
                      wage_df,
                      on="TEMPORARY_EMPLOYEE_ID",
                      how="inner")
    joined["ALLWAGES"] = (joined["REGWAGES"] +
                          joined["OTWAGES"] +
                          joined["OTHERWAGES"])
    joined["GOVERNMENT"] = (joined["DEPT_BRANCH_NM"]
                            .replace("Executive", "MN State")
                            .replace("Other", "MN State"))
    refined = joined[["GOVERNMENT",
                      "EMPLT_AGENCY_NM",
                      "DEPT_NM",
                      "JOB_DESC",
                      "ALLWAGES"]]
    refined.columns = ["GOVERNMENT", "AGENCY", "DEPT", "TITLE", "WAGES"]
    empl_nm = _split_name_col(joined["EMPL_NM"])
    refined = pd.concat([refined, empl_nm], axis=1)
    refined["YEAR"] = [year] * len(refined)
    refined.to_csv(output_file, index=False)


if __name__ == "__main__":
    arguments = docopt(__doc__)
    main(arguments["<input_file>"],
         arguments["<output_file>"],
         arguments["<year>"])

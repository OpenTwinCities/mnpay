from openpyxl import load_workbook
import pandas as pd

from . import utils


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


def _row_to_wage(row):
    return utils.Wage(
        first_name=row["FIRST_NAME"],
        last_name=row["LAST_NAME"],
        middle_name=row["MIDDLE_NAME"],
        government=row["GOVERNMENT"],
        agency=row["AGENCY"],
        dept=row["DEPT"],
        title=row["TITLE"],
        wage=row["WAGES"],
        year=row["YEAR"]
    )


def etl(input_file, year):
    wb = load_workbook(filename=input_file)
    yearpart = str(year)[2:]
    hr_df = _convert_ws_to_df(wb["FY"+yearpart+" HR INFO"])
    wage_df = _convert_ws_to_df(wb["FY"+yearpart+" EARNINGS"])
    joined = pd.merge(hr_df,
                      wage_df,
                      on="TEMPORARY_ID",
                      how="inner")
    joined["GOVERNMENT"] = (joined["BRANCH_NAME"]
                            .replace("Executive", "MN State")
                            .replace("Other", "MN State"))
    refined = joined[["GOVERNMENT",
                      "AGENCY_NAME",
                      "DEPARTMENT_NAME",
                      "JOB_TITLE",
                      "TOTAL_WAGES"]]
    refined.columns = ["GOVERNMENT", "AGENCY", "DEPT", "TITLE", "WAGES"]
    empl_nm = _split_name_col(joined["EMPLOYEE_NAME"])
    refined = pd.concat([refined, empl_nm], axis=1)
    refined["YEAR"] = year
    return [_row_to_wage(row) for _, row in refined.iterrows()]

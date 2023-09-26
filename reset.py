import openpyxl
from openpyxl import load_workbook


def reset():
    workbook = load_workbook(filename="snipeCounts/SnipeCount.xlsx")
    countsheet = workbook["counts"]
    logsheet = workbook["log"]

    countsheet.delete_rows(2, 10)
    logsheet.delete_rows(2, 10)

    logsheet["H1"] = 0

    workbook.save(filename="snipeCounts/SnipeCount.xlsx")
    workbook.close()


reset()

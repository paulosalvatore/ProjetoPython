from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws["A1"] = 42
wb.save("planilha1.xlsx")

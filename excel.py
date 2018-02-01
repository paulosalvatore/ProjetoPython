from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Página 1"
ws["A1"] = 1
wb.save("planilha.xlsx")

from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Cachorro"
ws2 = wb.create_sheet("Zebra")
ws3 = wb.create_sheet("Girafa")
ws4 = wb.create_sheet("Gato")

wb.save("planilha.xlsx")

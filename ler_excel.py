from openpyxl import load_workbook
wb = load_workbook(filename="planilha.xlsx")

ws = wb["Cachorro"]

ws.cell(
	column=1,
	row=1,
	value="A"
)

wb.save("planilha.xlsx")

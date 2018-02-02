from openpyxl import Workbook
from openpyxl.chart import Reference, BarChart3D
from openpyxl.chart.marker import DataPoint
from openpyxl.drawing.fill import PatternFillProperties, ColorChoice

wb = Workbook()
ws = wb.active
ws.title = "Página 1"

linhas = [
	["Casa Legislativa", "Alta", "Média", "Baixa", "Total"],
	["Titulo 1", 1, 2, 3, 1],
	["Titulo 2", 2, 2, 1, 4],
	["Titulo 3", 6, 2, 7, 8],
	["Titulo 4", 1, 2, 9, 4],
	["Titulo 5", 7, 2, 5, 6],
	["Titulo 6", 9, 2, 3, 3]
]

cores = [
	"000000",
	"00FF00",
	"FF0000",
	"0000FF"
]

for linha in linhas:
	ws.append(linha)

data = Reference(ws, min_col=2, min_row=1, max_col=5, max_row=7)
titles = Reference(ws, min_col=1, min_row=2, max_row=7)
chart = BarChart3D()
chart.title = "3D Bar Chart"
chart.add_data(data=data, titles_from_data=True)
chart.set_categories(titles)

for indice, cor in enumerate(cores):
	chart.series[indice].graphicalProperties.solidFill = cor

ws.add_chart(chart, "G5")

wb.save("planilha.xlsx")

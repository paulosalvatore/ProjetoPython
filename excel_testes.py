from openpyxl import Workbook

wb = Workbook()
ws = wb.active

data = [
    ["Fruta", "Quantidade"],
    ["Kiwi", 3],
    ["Uva", 15],
    ["Maçã", 7]
]

for row in data:
    ws.append(row)

ws.auto_filter.ref = "A1:B4"
ws.auto_filter.add_filter_column(0, ["Kiwi", "Maçã"])
ws.auto_filter.add_sort_condition("B2:B4")

wb.save("filtered.xlsx")

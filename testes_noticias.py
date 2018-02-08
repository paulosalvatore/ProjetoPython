import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Notícias do Senado"

def limpar_espacos(texto):
	return texto.strip()


def pegar_url(pagina):
	return "http://www25.senado.leg.br/web/atividade/materias/-/materia/autor/5012/p/{}/o/3".format(pagina)

link = pegar_url(1)
conteudo = requests.get(link)
soup = BeautifulSoup(conteudo.text, "html.parser")

anchors = soup.find_all("a")

ultima_pagina = 1

for a in anchors:
	if a.text == "Última":
		href = a.get("href")
		href = href.split("/")
		ultima_pagina = int(href[href.index("p") + 1])

for pagina in range(ultima_pagina):
	pagina += 1

	if pagina > 1:
		link = pegar_url(pagina)
		conteudo = requests.get(link)
		soup = BeautifulSoup(conteudo.text, "html.parser")

	div_zebra = soup.find_all("div", {"class": "div-zebra"})

	dls = div_zebra[0].find_all("dl")
	for dl in dls:
		dts = dl.find_all("dt")
		dds = dl.find_all("dd")

		for indice, dt in enumerate(dts):
			dd = dds[indice]
			ws.append(
				[
					limpar_espacos(dt.text),
					limpar_espacos(dd.text)
				]
			)
		ws.append([])

wb.save("noticias.xlsx")

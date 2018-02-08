import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def pegar_argumento_url(url, buscar_argumento):
	o = urlparse(url)

	argumentos = o.query.split("&")

	for argumento in argumentos:
		informacao = argumento.split("=")
		chave = informacao[0].replace("_materia_WAR_atividadeportlet_", "")
		valor = informacao[1]
		if chave == buscar_argumento:
			return valor


def pegar_url(autor, pagina):
	autor = autor.replace(" ", "+")
	url = "http://www25.senado.leg.br/web/atividade/materias?p_p_id=materia_WAR_atividadeportlet&p_p_lifecycle=0&_materia_WAR_atividadeportlet_ufAutor=&_materia_WAR_atividadeportlet_tipo=&_materia_WAR_atividadeportlet_pesquisaAvancada=true&_materia_WAR_atividadeportlet_tipoAutor=&_materia_WAR_atividadeportlet_numero=&_materia_WAR_atividadeportlet_situacaoTramitacao=T&_materia_WAR_atividadeportlet_anoNorma=&_materia_WAR_atividadeportlet_palavraChave=&_materia_WAR_atividadeportlet_textoTramitacao=&_materia_WAR_atividadeportlet_assunto=&_materia_WAR_atividadeportlet_relator=&_materia_WAR_atividadeportlet_tipoNorma=&_materia_WAR_atividadeportlet_partidoAutor=&_materia_WAR_atividadeportlet_codSituacaoTramitacao=&_materia_WAR_atividadeportlet_numeroNorma=&_materia_WAR_atividadeportlet_natureza=&_materia_WAR_atividadeportlet_ativos=on&_materia_WAR_atividadeportlet_ano=&_materia_WAR_atividadeportlet_inicioApresentacao=&_materia_WAR_atividadeportlet_codComissao=&_materia_WAR_atividadeportlet_autor={}&_materia_WAR_atividadeportlet_localPalavraChave=&_materia_WAR_atividadeportlet_fimApresentacao=&_materia_WAR_atividadeportlet_btnSubmit=&_materia_WAR_atividadeportlet__complementar=on&_materia_WAR_atividadeportlet_p={}".format(autor, pagina)
	return url


def pegar_ultima_pagina(autor):
	url = pegar_url(autor, 1)
	conteudo = requests.get(url)
	conteudo_principal = BeautifulSoup(conteudo.text, "html.parser")
	ancoras = conteudo_principal.find_all("a")
	for ancora in ancoras:
		if ancora.text == "Última":
			ultima_pagina = int(pegar_argumento_url(ancora.get("href"), "p"))
			return ultima_pagina


autor = "Davi Alcolumbre"
ultima_pagina = pegar_ultima_pagina(autor)

for pagina in range(ultima_pagina):
	pagina += 1
	print(pagina)

	url = pegar_url(autor, pagina)
	conteudo = requests.get(url)
	conteudo_principal = BeautifulSoup(conteudo.text, "html.parser")

	div_zebra = conteudo_principal.find("div", {"class": "div-zebra"})

	dls = div_zebra.find_all("dl")

	for dl in dls:
		dts = dl.find_all("dt")
		dds = dl.find_all("dd")

		for indice, dt in enumerate(dts):
			dd = dds[indice]

			print(dt.text.strip())
			print(dd.text.strip())

			anchor = dd.find("a")

			if anchor:
				link = anchor.get("href")
				print(link)

			print()

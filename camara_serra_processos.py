import requests
from bs4 import BeautifulSoup
import urllib


def download_file(url, arquivo):
	urllib.request.urlretrieve(url, arquivo)


radicalUrl = "http://www3.camaraserra.es.gov.br"
urlBase = radicalUrl + "/spl/consulta-producao.aspx?termo="
termo = "Caixa"
urlCompleta = urlBase + urllib.parse.quote(termo)
# print(urlCompleta)
conteudo = requests.get(urlCompleta)
conteudo_principal = BeautifulSoup(conteudo.text, "html.parser")
# print(conteudo_principal)

"""
Tabela #tabela
Entrar no tbody
Entrar em cada TR do tbody, que corresponde a um processo
Pular o primeiro TR
"""

# tabela = conteudo_principal.find("table", {"id": "tabela"})
trs = conteudo_principal.find_all("tr")
del trs[0]
# print(len(trs))

def formatar_indicacao(indicacao):
	indicacao = indicacao.replace("Projeto de Lei ", "PL_")
	indicacao = indicacao.replace("PROPOSIÇÃO", "")
	indicacao = indicacao.replace("/", "_")
	return indicacao.strip()


diretorio = "arquivos/"


for tr in trs:
	ancora = tr.find("a")
	href = ancora["href"]
	href = href.replace("processo.aspx?id=", "")
	href = href.split("&")
	id = href[0]
	id = "52827"
	print(id)
	urlPdf = "http://www3.camaraserra.es.gov.br/Sistema/Protocolo/Processo2/Digital.aspx?id=" + id
	urlDetalhes = "http://www3.camaraserra.es.gov.br/processo.aspx?id=" + id
	print(urlPdf)
	print(urlDetalhes)
	print()

	conteudoUrlDetalhes = requests.get(urlDetalhes)
	conteudoUrlDetalhesSoup = BeautifulSoup(conteudoUrlDetalhes.text, "html.parser")

	h3 = conteudoUrlDetalhesSoup.find("h3")
	indicacao = formatar_indicacao(h3.text)

	ementa = conteudoUrlDetalhesSoup.find("p", {"id": "ContentPlaceHolder1_p_ementa"})
	ementa = ementa.text.replace("Ementa: ", "").strip()

	autoria = conteudoUrlDetalhesSoup.find("p", {"id": "ContentPlaceHolder1_p_autoria"})
	autoria = autoria.text.strip()

	historicoTbody = conteudoUrlDetalhesSoup.find("tbody", {"id": "ContentPlaceHolder1_tb_tramitacao"})
	historicoTrs = historicoTbody.find_all("tr")
	historico = []

	for historicoTr in historicoTrs:
		table = historicoTr.find("table")
		if table:
			historico_item = []
			tableTds = table.find_all("td")

			for td in tableTds:
				if len(td.text) > 0:
					historico_item.append(td.text)

			historico.append(historico_item)

	conteudoUrlPdf = requests.get(urlPdf)
	conteudoUrlPdfSoup = BeautifulSoup(conteudoUrlPdf.text, "html.parser")

	ancorasPdf = conteudoUrlPdfSoup.find_all("a")
	for ancoraPdf in ancorasPdf:
		if ancoraPdf.has_attr("data-pdf") > 0:
			href = ancoraPdf["data-pdf"]
			nome_href = ancoraPdf.text.strip().replace("/", "_").replace(".", "_")
			if nome_href == "clicar aqui para baixar o arquivo PDF_":
				continue
			urlPdfCompleta = radicalUrl + href
			nomeArquivo = "{0} - {1}".format(indicacao, nome_href)
			#download_file(urlPdfCompleta, diretorio + nomeArquivo + ".pdf")


	"""
	Dentro da URL de Detalhes, precisamos pegar algumas informações
	Data da Apresentação
	Ementa
	Autoria
	Pegar Indicação
	Histórico de Tramitação (vários itens)
	"""

	break

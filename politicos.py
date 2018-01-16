import requests
import json

id_politico = 1  # int(input("Digite uma ID: "))  # Exemplo: 1
url = "http://politicos.olhoneles.org/api/v0/politicians/{}".format(id_politico)
conteudo_url = requests.get(url)
conteudo_json = json.loads(conteudo_url.text)
print(conteudo_json)


def varrer_lista_dicionarios(lista, chave, exibicao):
	print(exibicao + ":")
	for item in lista:
		print("\t" + item[chave])


def formatar_booleano(variavel):
	if variavel:
		return "Sim"
	else:
		return "Não"


def pegar_valor_dicionario(caminho, base):
	try:
		for item in caminho:
			base = base[item]
	except:
		base = "Valor não informado"
	return base


nomes_alternativos = conteudo_json["alternative_names"]
varrer_lista_dicionarios(nomes_alternativos, "name", "Nomes Alternativos")
print()

candidaturas = conteudo_json["candidacies"]
print("Candidaturas:")
for indice, candidatura in enumerate(candidaturas):
	valor = pegar_valor_dicionario(["candidacy_status", "name"], candidatura)
	print(valor)
	"""print("{}ª Candidatura:".format(indice + 1))
	status = candidatura["candidacy_status"]["name"]
	print("\tStatus: " + status)
	eleito = formatar_booleano(candidatura["elected"])
	print("\tEleito: " + eleito)
	print()"""


"""
Nomes Alternativos  alternative_names   name

Candidaturas    candidacies
	Status  candidacy_status    name
	Cidade  city    name
	Eleito  elected
	Cargo   political_office    name
	Estado  state   name

CPF     cpf
Etnia   ethnicity   name
"""

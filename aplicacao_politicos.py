import requests
import json


def formatar_cpf(cpf):
	return "{}.{}.{}-{}".format(cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])


id_politico = 1  # int(input("Digite uma ID: "))  # Exemplo: 1
url = "http://politicos.olhoneles.org/api/v0/politicians/{}".format(id_politico)
conteudo_url = requests.get(url)
conteudo_json = json.loads(conteudo_url.text)
print(conteudo_json)

conteudo_json["cpf"] = formatar_cpf(conteudo_json["cpf"])

config = [
	{
		"nome": "Nomes Alternativos",
		"campo": "alternative_names",
		"tipo": list,
		"valor": [
			{
				"campo": "name",
				"tipo": str,
				"exibir_nome_campo": False
			}
		]
	},
	{
		"nome": "CPF",
		"campo": "cpf",
		"tipo": str
	},
	{
		"nome": "Candidaturas",
		"campo": "candidacies",
		"tipo": list,
		"exibicao_item": "Candidatura",
		"valor": [
			{
				"nome": "Status",
				"campo": "candidacy_status",
				"tipo": dict,
				"valor": [
					{
						"campo": "name",
						"tipo": str
					}
				]
			},
			{
				"nome": "Cidade",
				"campo": "city",
				"tipo": dict,
				"valor": [
					{
						"campo": "name",
						"tipo": str
					}
				]
			},
			{
				"nome": "Estado",
				"campo": "state",
				"tipo": dict,
				"valor": [
					{
						"campo": "siglum",
						"tipo": str
					}
				]
			},
			{
				"nome": "Cargos",
				"campo": "institution",
				"tipo": dict,
				"valor": [
					{
						"nome": "Cargo",
						"campo": "political_offices",
						"tipo": list,
						"valor": [
							{
								"campo": "name",
								"tipo": str
							}
						]
					}
				]
			},
			{
				"nome": "Eleito",
				"campo": "elected",
				"tipo": bool
			}
		]
	}
]


def exibir_item(item, base=False, item_anterior=""):
	if base is False:
		base = conteudo_json

	try:
		if not item["campo"] is False:
			base = base[item["campo"]]
	except:
		base = "Valor não encontrado."
		item["tipo"] = str

	if item["tipo"] == list:
		indice = 1

		for atributo in base:
			if "exibicao_item" in item:
				print("{}ª {}".format(indice, item["exibicao_item"]))

			if "valor" in item:
				indice += 1

				for valor in item["valor"]:
					exibir_item(valor, atributo, item)

				if indice < len(item["valor"]):
					print()
			else:
				novo_item = item.copy()
				novo_item["tipo"] = str
				novo_item["campo"] = False
				exibir_item(novo_item, atributo, item)

	elif item["tipo"] == dict:
		for valor in item["valor"]:
			exibir_item(valor, base, item)
	elif item["tipo"] == str or item["tipo"] == bool:
		if item["tipo"] == bool:
			base = "Sim" if base else "Não"
			item_anterior = item

		if ("nome" in item_anterior and
			not ("exibir_nome_campo" in item and not item["exibir_nome_campo"])):
			print("\t" + item_anterior["nome"] + ": " + base)
		else:
			print("\t" + base)

for item in config:
	print(item["nome"])
	exibir_item(item)

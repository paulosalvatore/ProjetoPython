import requests
import json

id = 1 # int(input("Digite uma ID: "))  # Exemplo: 1
url = "http://politicos.olhoneles.org/api/v0/politicians/{}".format(id)
conteudo_url = requests.get(url)
conteudo_json = json.loads(conteudo_url.text)
print(conteudo_json)
# Exiba as informações do político a partir da ID

"""
Político:
Nomes alternativos:
	Professor Edileudo
CPF: 233.293.352-20
Candidaturas:
	1ª Candidatura:
		Vereador
		Cidade/Estado: Rio Branco/AC
		Data: 01/10/2000
		Status: Deferido
		Eleito: Não
"""

config = {
	"Nomes Alternativos": {
		"alternative_names": [
			{
				"name": ""
			}
		]
	},
	"Candidaturas - Status": {
		"candidacies": [
			{
				"candidacy_status": {
					"name": ""
				}
			}
		]
	},
	"Candidaturas - Cidades": {
		"candidacies": [
			{
				"city": {
					"name": ""
				}
			}
		]
	}
}


def teste(caminho, base=None):
	if not base:
		base = conteudo_json
	if type(caminho) == dict:
		for chave, valor in caminho.items():
			if type(chave) == str:
				base = base[chave]
				teste(valor, base)
	elif type(caminho) == list:
		for chave, valor in enumerate(caminho):
			for elemento in base:
				teste(valor, elemento)
	elif type(caminho) == str:
		print("\t" + base)

for exibicao, caminho in config.items():
	print(exibicao + ":")
	teste(caminho)

"""
Varrer o dicionário de config
Exibição do campo é o index
O valor do do dicionário determina como iremos varrer
Se o tipo do valor for uma lista, devemos varrer a lista
Se o tipo do valor for um dicionário, devemos varrer o dicionário
Se o tipo for string, exibimos a informação
"""

"""
def pegar_valor(caminho, base=None):
	if not base:
		base = conteudo_json

	tipo_caminho = type(caminho)

	if tipo_caminho == list:
		print("Tipo do caminho é uma lista")
		# Varrer lista da base, correspondente
	elif tipo_caminho == dict:
		print("Tipo do caminho é uma dicionário")
	else:
		valor = base[caminho]
		print("Tipo do caminho é outra coisa")

	return valor

for exibicao, caminho in config.items():
	base = conteudo_json
	print(exibicao + ":")
	for item in caminho:
		tipo_base = type(base)
		if tipo_base == dict:
			base = base.get(item)
			# print(base)
		elif tipo_base == list:
			# print("Varrer nova base", base)
			nova_base = base
			for elemento in base:
				# print(elemento)
				nova_base = elemento[item]
				print("\t" + nova_base)
"""

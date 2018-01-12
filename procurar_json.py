import requests
import json

# Pegar palavra digitada pelo usuário
palavra = input("Digite uma palavra: ")
# Inserir palavra na base_url, no lugar de {query}
# Primeira maneira (mais prática)
base_url = "https://api.chucknorris.io/jokes/search?query={}".format(palavra)

# Segunda maneira
base_url = "https://api.chucknorris.io/jokes/search?query={query}"
base_url = base_url.replace("{query}", palavra)

# Terceira maneira
base_url = "https://api.chucknorris.io/jokes/search?query=" + palavra

# Quarta maneira
base_url = "https://api.chucknorris.io/jokes/search?query="
base_url += palavra

# Pegar o conteúdo dessa URL utilizando o requests
conteudo = requests.get(base_url)

# Transformar o conteúdo em JSON
conteudo_json = json.loads(conteudo.text)

# Exibir na tela a quantidade de piadas encontradas
total = conteudo_json["total"]
print("A busca por '{}' encontrou {} piadas.".format(palavra, total))

piadas = conteudo_json["result"]


def exibir_piada(piada, campo="value"):
	print(piada[campo])


def exibir_piada_pelo_indice(lista_piadas, indice):
	exibir_piada(lista_piadas[indice])


def exibir_piadas(lista_piadas):
	for indice, piada in enumerate(lista_piadas):
		# exibir_piada_pelo_indice(lista_piadas, indice)  # Exibir pelo índice
		exibir_piada(piada)  # Exibir direto o dicionário da piada

# exibir_piadas(piadas)
# exibir_piada(piadas[0], "id")

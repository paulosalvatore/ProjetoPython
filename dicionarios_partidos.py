
partidos = {
	"PT": {
		"nome": "Partido dos Trabalhadores",
		"sede": "Brasília",
		"presidente": "Gleisi Hoffmann",
		"numero_eleitoral": 13,
		"candidato_proprio": True,
		"ideologias": [
			"Socialismo democrático",
			"Desenvolvimentismo",
			"Lulismo",
			"Trotskismo",
			"Democracia"
		]
	},
	"PV": {
		"nome": "Partido Verde",
		"sede": "São Paulo",
		"presidente": "José Luiz Penna",
		"numero_eleitoral": 43,
		"candidato_proprio": False,
		"ideologias": [
			"Ambientalismo",
			"Ecologismo",
			"Liberalismo social",
			"Progressismo",
			"Social democracia",
			"Democracia"
		]
	}
}

"""
def contar_ideologias(partido):
	return len(partidos[partido]["ideologias"])

sigla_partido = "PV"

quantidade_ideologias = contar_ideologias(sigla_partido)

print("O partido {} possui {} ideologias.".format(sigla_partido, quantidade_ideologias))
"""


# Declaramos a função 'procurar_partidos_idelogia' que recebe
# uma ideologia e busca no dicionário de partidos quais possuem
# aquela ideologia, armazenando-os em uma lista nova e retornando
# isso para fora da função
def procurar_partidos_ideologia(ideologia):
	# Declaramos uma lista vazia chamada 'lista_partidos'
	lista_partidos = []
	# Varremos o dicionário de 'partidos' e armazenamos cada
	# sigla de partido sob a variável 'partido'
	for partido in partidos:
		# Pegamos a lista de ideologias do partido, acessando o
		# caminho específico do dicionário de partidos
		# partidos -> sigla do partido -> ideologias
		ideologias = partidos[partido]["ideologias"]
		# Checamos se a lista de ideologias possui a ideologia
		# em questão recebida pelo argumento da função
		checagem_ideologia = ideologias.count(ideologia)
		# Caso a checagem seja maior do que 0, executamos
		# o conteúdo do if
		if checagem_ideologia > 0:
			# Adicionamos a sigla no partido na lista nova que
			# foi criada anteriormente chamada 'lista_partidos'
			lista_partidos.append(partido)
	# Assim que terminar o for, retornamos a lista de partidos
	# criada com todos os partidos que possuem aquela ideologia
	# passada na função
	return lista_partidos

partidos_democracia = procurar_partidos_ideologia("Democracia")
# Irá retornar uma lista com ["PT", "PV"]
print(partidos_democracia)

partidos_socialismo = procurar_partidos_ideologia("Socialismo democrático")
# Irá retornar uma lista com ["PT"]
print(partidos_socialismo)

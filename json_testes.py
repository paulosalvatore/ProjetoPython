
"""
import json

lista = [
	1,
	2,
	3,
	{
		'4': 5,
		'6': 7
	}
]

print(lista)
print(type(lista))

string_json = json.dumps(lista)
print(string_json)
print(type(string_json))

texto = '[1, 2, 3, {"4": 5, "6": 7}]'
print(type(texto))
lista_json = json.loads(texto)
print(lista_json)
print(type(lista_json))
print(lista_json[0])
print(lista_json[1])
print(lista_json[2])
print(type(lista_json[3]))

dicionario = {
	"teste1": 1,
	"teste2": 2,
	"teste3": 3
}

for key, value in dicionario.items():
	print(key)
	print(value)


def somar_tudo(*numeros, exibir=False):
	total = sum(numeros)
	if exibir:
		print(total)
	return total

somar_tudo(1, 2, 3, 4, 5, 6, 7, 8, 9, exibir=False)


def exibir_lista(lista, exibir_chaves=False):
	for chave in range(len(lista)):
		item = lista[chave]
		if exibir_chaves:
			print("Chave: {}, Item: {}".format(chave, item))
		else:
			print("Item: {}".format(item))
	print()

lista = [1, 2, 3, 4, 5]
exibir_lista(lista)
exibir_lista(lista, True)

lista1 = [1, 2, 3]
tupla = 1,
lista2 = list(tupla)
print(lista2)
lista2[0] = 5
print(lista2)
print(type(lista2))
range1 = range(6)
print()
a = list((1, 2, 3))
print(a)
print(type(a))

teste = range(2, 7, 2)
print(list(teste))

arvores = range(5, 100, 2)
print(len(list(arvores)) * 10)

import tuplas

print(tuplas.teste())
"""


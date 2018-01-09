from random import randint

while True:
	lista = [1, 2, 3, 4, 5, 6]

	indice_aleatorio = randint(0, len(lista) - 1)
	elemento_aleatorio = lista[indice_aleatorio]
	print(elemento_aleatorio)

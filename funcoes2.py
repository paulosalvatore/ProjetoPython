def criar_lista(quantidade_elementos):
	lista = []

	for numero in range(quantidade_elementos):
		numero_digitado = int(input("Número: "))
		lista.append(numero_digitado)

	print(lista)

	return lista


def somar_numero_na_lista(lista, numero):
	for indice in range(len(lista)):
		lista[indice] = lista[indice] + numero


nova_lista = criar_lista(2)
somar_numero_na_lista(nova_lista, 1)
somar_numero_na_lista(nova_lista, 3)
print(nova_lista)




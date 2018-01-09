def exibir_lista(lista, exibir_chave=False):
	for chave in range(len(lista)):
		valor = lista[chave]
		if exibir_chave:
			print("{}: {}".format(chave, valor))
		else:
			print("{}".format(valor))

numeros = [10, 5, 6, 7, 9, 10]
# exibir_lista(numeros, True)


def somar_tudo(*numeros, exibir=False):
	total = sum(numeros)
	if exibir:
		print(total)
	return total

resultado = somar_tudo(1, 2, 3, 4, 5, 6, 7, exibir=True)

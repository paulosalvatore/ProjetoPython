def somar(a, b, exibir=False):
	total = a + b

	if exibir:
		print(total)

	return total

numero1 = 10
numero2 = 20
resultado = somar(numero1, numero2, False)


def exibir(lista, exibir_chaves=False):
	for chave in range(len(lista)):
		item = lista[chave]
		if exibir_chaves:
			print("Chaves: {}, Valor: {}".format(chave, item))
		else:
			print("Valor: {}".format(item))

numeros = [1, 2, 3, 4, 5, 1, 2, 6, 7]
exibir(numeros, exibir_chaves=True)

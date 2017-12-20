def criar_lista(quantidade_numeros):
	print("criar lista")
	lista = []
	for numero in range(quantidade_numeros):
		numero_digitado = int(input("Digite o {}º número: ".format(numero + 1)))
		lista.append(numero_digitado)
	return lista

quantidade_numeros_usuario = int(input("Quantos números: "))
lista1 = criar_lista(quantidade_numeros_usuario)
print(lista1)
print(len(lista1))


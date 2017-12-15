lista = [1, 1, 2, 2, 3, 4, 5, 6, 1, 1]
lista_vazia = []

for numero in lista:
	if lista_vazia.count(numero) == 0:
		lista_vazia.append(numero)
		quantidade_ocorrencias = lista.count(numero)
		if quantidade_ocorrencias > 1:
			print("O número {} está presente {} vezes na lista.".format(numero, quantidade_ocorrencias))
		else:
			print("O número {} não está repetido na lista.".format(numero))

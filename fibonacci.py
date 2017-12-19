numero_elementos = int(input("Digite a quantidade de elementos: "))

lista = [1, 1]
for numero in range(numero_elementos):
	novo_numero = lista[numero] + lista[numero + 1]
	lista.append(novo_numero)

print("A sequência de Fibonacci com {} elementos é:\n{}.".format(numero_elementos, lista))

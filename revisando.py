"""
def somar(*numeros):
	total = 0

	for numero in numeros:
		total += numero

	return total


def somar_range(*numeros):
	total = 0

	for indice in range(len(numeros)):
		numero = numeros[indice]
		total += numero

	return total

resultado = somar(1, 2, 3, 4)
print(resultado)
resultado = somar_range(1, 2, 3, 4, 5)
print(resultado)
"""

"""
def potencia(base, expoente):  # Adicione os parâmetros aqui
	resultado = base ** expoente
	return resultado
	# print("{} elevado a {} é {}.".format(base, expoente, resultado))

resultado_potencia = potencia(2, 3)  # Adicione os argumentos aqui
# Exibe o resultado da potência + 1
print(resultado_potencia + 1)
"""


"""
def contar_numeros_pequenos(numeros):
	total = 0

	for numero in numeros:
		if numero < 10:
			total += numero

	return total

lista = [1, 2, 3, 4]
resultado = contar_numeros_pequenos(lista)
print("O resultado é {}.".format(resultado))
"""

"""
politicos = {
	"Temer": "PMDB",
	"Lula": "PT",
	"Aécio": "PSDB"
}

for politico in politicos:
	partido = politicos[politico]
	print(partido)
"""

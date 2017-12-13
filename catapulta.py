pedras_minuto = 300 / (5 * 15)

baterias = int(input("Quantas baterias? "))
minutos = int(input("Quantos minutos? "))

pedras = int(baterias * minutos * pedras_minuto)

print(
	"A catapulta lançou {} pedras em {} baterias de {} minutos, cada."
	.format(pedras, baterias, minutos)
)

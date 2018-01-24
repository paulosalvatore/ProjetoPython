
def formatar_plural(quantidade, palavra):
	plural = "" if abs(quantidade) == 1 else "s"

	return "{}{}".format(palavra, plural)

numero = int(input("Número: "))
plural = "" if abs(numero) == 1 else "s"

print("Tenho {} {}.".format(numero, formatar_plural(numero, "gatinho")))

"""
animal = ""

if numero == 1:
	animal = "Gato"
else:
	animal = "Cachorro"

print(animal)

"""

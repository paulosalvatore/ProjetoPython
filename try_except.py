try:
	numero = int(input("Digite um número: "))
	print("Número digitado corretamente.")
except Exception as e:
	print("Um erro ocorreu: {}.".format(e))

def exibir_lista(lista, exibir_chave=False):
	for chave, valor in enumerate(lista):
		if exibir_chave:
			print("{}: {}".format(chave, valor))
		else:
			print("{}".format(valor))


def pegar_string(mensagem, obrigatorio=True, minimo=0):
	texto = ""
	while texto == "":
		texto = input(mensagem)

		if not obrigatorio and (len(texto) == 0 or len(texto) >= minimo):
			break

		if len(texto) < minimo:
			texto = ""
			print("Digite pelo menos {} caracteres.".format(minimo))

	return texto


def pegar_inteiro(mensagem):
	numero = ""

	while numero == "":
		try:
			numero = int(input(mensagem))
		except Exception as erro:
			# print("Erro: {}".format(erro))
			print("Digite um número válido.")

	return numero

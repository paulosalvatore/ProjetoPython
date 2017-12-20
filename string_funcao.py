
def checar_ocorrencias(texto, checar_letra):
	numero_ocorrencias = 0
	for indice in range(len(texto)):
		letra = texto[indice]
		if checar_letra == letra:
			numero_ocorrencias = numero_ocorrencias + 1
	return numero_ocorrencias


texto_usuario = input("Digite um texto: ")
letra_usuario = input("Digite uma letra: ")
ocorrencias = checar_ocorrencias(texto_usuario, letra_usuario)
print("A letra '{}' está presente {} vezes no texto '{}'.".format(letra_usuario, ocorrencias, texto_usuario))


def checar_ocorrencias_count(texto, checar_letra):
	return texto.count(checar_letra)

print("A letra '{}' está presente {} vezes no texto '{}'.".format(letra_usuario, ocorrencias, texto_usuario))

ocorrencias_split = texto_usuario.split(letra_usuario)
print("A letra '{}' está presente {} vezes no texto '{}'.".format(letra_usuario, len(ocorrencias_split) - 1, texto_usuario))

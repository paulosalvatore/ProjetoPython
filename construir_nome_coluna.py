letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def pegar_nome_coluna(coluna):
	resto = coluna % len(letras)
	letra_pegar = 26 if resto == 0 else resto
	letra = letras[letra_pegar - 1]
	total = coluna // len(letras)
	nome_coluna = ""

	if total > 1 and resto == 0:
		nome_coluna += pegar_nome_coluna(total - 1)
	elif total > 0 and resto > 0:
		nome_coluna += pegar_nome_coluna(total)

	nome_coluna += letra

	return nome_coluna

for i in range(1, 1500):
	nome = pegar_nome_coluna(i)
	print(i, nome, " ")

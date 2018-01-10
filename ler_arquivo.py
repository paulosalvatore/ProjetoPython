arquivo = open("usuario.txt", "r")
conteudo_arquivo = arquivo.read()
print(conteudo_arquivo)
linhas = conteudo_arquivo.split("\n")

usuario = {}


def tratar_chave(chave_recebida):
	chave_recebida = chave_recebida.lower()
	chave_recebida = chave_recebida.replace(" de ", " ")
	chave_recebida = chave_recebida.replace(" ", "_")
	return chave_recebida


def checar_inteiro(valor_recebido):
	try:
		valor_recebido = int(valor_recebido)
	except:
		pass

	return valor_recebido


def tratar_valor(valor_recebido):
	valor_recebido = checar_inteiro(valor_recebido)
	return valor_recebido


for linha in linhas:
	informacao_quebrada = linha.split(": ")
	if len(informacao_quebrada) >= 2:
		chave = tratar_chave(informacao_quebrada[0])
		valor = tratar_valor(informacao_quebrada[1])
		usuario[chave] = valor

print(usuario)
arquivo.close()

"""
linha = arquivo.readline()
while linha:
	print(linha)
	linha = arquivo.readline()
"""

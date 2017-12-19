arquivo = open("arquivo.txt", "r")
conteudo_arquivo = arquivo.read()
print(conteudo_arquivo)
arquivo.close()

arquivo = open("arquivo.txt", "r")
line = arquivo.readline()
while line:
	print(line)
	line = arquivo.readline()

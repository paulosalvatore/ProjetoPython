import tkinter as tk
from tkinter import filedialog


def limpar_linha(linha):
	return linha.replace("\n", "")


root = tk.Tk()
root.withdraw()

# caminho_arquivo = filedialog.askopenfilename()
caminho_arquivo = "C:/Users/paulo/Desktop/vereador.txt"

arquivo = open(caminho_arquivo, "r")
linha = limpar_linha(arquivo.readline())

titulos = linha.split("#")
for chave, titulo in enumerate(titulos):
	titulo_separado = titulo.split("^")
	titulos[chave] = titulo_separado

while linha:
	linha = limpar_linha(arquivo.readline())
	valores = linha.split("#")
	for chave, valor in enumerate(valores):
		valor_separado = valor.split("^")
		if chave < len(titulos):
			titulo = titulos[chave]
			print(titulo, valor_separado)
	# print(linha)

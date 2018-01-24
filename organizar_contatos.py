import time
from openpyxl import Workbook

inicio = time.clock()

arquivo = open("contatos.txt", "r")
linha = arquivo.readline()

contatos = []
contatos_sem_email = []

nome = ""
email = ""


def atualizar_contato_existente(nome, email):
	for contato in contatos:
		if contato["nome"] == nome:
			if contato["email"].count(email) == 0:
				contato["email"].append(email)
			return True

	return False

while linha:
	linha = linha.replace("\n", "")

	if linha != "":
		if linha.count("@") == 0:
			if nome != "" and contatos_sem_email.count(nome) == 0:
				contatos_sem_email.append(nome)

			nome = linha
		else:
			email = linha

			contato = {
				"nome": nome,
				"email": [
					email
				]
			}

			if not atualizar_contato_existente(nome, email) and contatos.count(contato) == 0:
				contatos.append(contato)

			nome = ""
			email = ""

	linha = arquivo.readline()

wb = Workbook()
ws = wb.active

ws.append(
	[
		"Nome",
		"E-mail"
	]
)

for contato in contatos:
	# ws["A1"] = 42
	linha = [
		contato["nome"]
	]

	for email in contato["email"]:
		linha.append(email)

	ws.append(linha)

wb.save("planilha1.xlsx")

final = time.clock() - inicio

print("Excel gravado com sucesso em {:.2f} segundos.".format(final))

print("Aplicação finalizará após 3 segundos...")

time.sleep(3)

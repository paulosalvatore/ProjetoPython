import time

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

for contato in contatos:
	print(contato)

final = time.clock() - inicio

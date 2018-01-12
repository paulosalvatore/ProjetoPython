arquivo = open("contatos.txt", "r")

nome = ""
email = ""

nomes = ""
emails = ""
lista_nomes = []
lista_emails = []

usuarios_sem_email = ""
lista_usuarios_sem_email = []

linha = arquivo.readline()

while linha:
	linha = linha.replace("\n", "")

	if linha.count("@") > 0:
		email = linha

		if lista_nomes.count(nome) == 0 and lista_emails.count(email) == 0:
			nomes += nome + "\n"
			emails += email + "\n"

			lista_nomes.append(nome)
			lista_emails.append(email)

		nome = ""
		email = ""
	elif len(linha) > 0:
		if nome != "" and lista_usuarios_sem_email.count(nome) == 0:
			lista_usuarios_sem_email.append(nome)
			usuarios_sem_email += nome + "\n"

		nome = linha

	try:
		linha = arquivo.readline()
	except:
		pass

arquivo.close()

usuarios_nomes = open("usuarios_nomes.txt", "w")
usuarios_nomes.write(nomes)
usuarios_nomes.close()

usuarios_emails = open("usuarios_emails.txt", "w")
usuarios_emails.write(emails)
usuarios_emails.close()

usuarios_sem_email_arquivo = open("usuarios_sem_email.txt", "w")
usuarios_sem_email_arquivo.write(usuarios_sem_email)
usuarios_sem_email_arquivo.close()

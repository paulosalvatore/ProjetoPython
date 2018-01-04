paulo = {
	"nome": "Paulo Salvatore",
	"atividades": [10.0, 8.0, 7.5],
	"quizzes": [8.5, 9.0, 6.5],
	"testes": [5.0, 9.5]
}

luisa = {
	"nome": "Luísa Oliveira",
	"atividades": [7.0, 6.0, 9.5],
	"quizzes": [6.0, 8.0, 7.0],
	"testes": [1.5, 8.5]
}

ana = {
	"nome": "Ana Lúcia",
	"atividades": [9.0, 10.0, 4.5],
	"quizzes": [4.5, 2.0, 8.0],
	"testes": [1.0, 1.0]
}

estudantes = [paulo, luisa, ana]


def media(numeros):
	total = sum(numeros)
	return total / len(numeros)


def pegar_media(aluno):
	media_atividades = media(aluno["atividades"])
	media_quizzes = media(aluno["quizzes"])
	media_testes = media(aluno["testes"])

	total = (media_atividades * 0.1) + (media_quizzes * 0.3) + (media_testes * 0.6)

	return total


def checar_aprovacao(aluno):
	nome = aluno["nome"]
	media_calculada = pegar_media(aluno)

	print("Aluno: {} - Média: {:.2f}".format(nome, media_calculada))

	if media_calculada < 4.0:
		print("\t{} foi reprovado.".format(nome))
	elif media_calculada < 6:
		print("\t{} está de exame.".format(nome))
	else:
		print("\t{} está aprovado.".format(nome))

	print()


def pegar_media_classe(alunos_classe):
	medias_alunos_classe = []

	for aluno_classe in alunos_classe:
		media_calculada = pegar_media(aluno_classe)
		medias_alunos_classe.append(media_calculada)

	media_classe = media(medias_alunos_classe)

	return media_classe

for estudante in estudantes:
	checar_aprovacao(estudante)

media_classe_calculada = pegar_media_classe(estudantes)
print("Média da Classe: {:.2f}".format(media_classe_calculada))

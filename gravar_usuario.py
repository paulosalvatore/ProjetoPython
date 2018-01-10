nome = input("Nome: ")
idade = input("Idade: ")

arquivo = open("usuario.txt", "w")
arquivo.write("Nome: {}\n".format(nome))
arquivo.write("Idade: {}".format(idade))
arquivo.close()

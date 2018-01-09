import funcoes_basicas

lista = [1, 2, 3, 4, 5]

funcoes_basicas.exibir_lista(lista, True)

texto = funcoes_basicas.pegar_string("Texto: ")
print("Texto digitado: '{}'.".format(texto))

numero = funcoes_basicas.pegar_inteiro("Inteiro: ")
print("Número digitado: '{}'.".format(numero))

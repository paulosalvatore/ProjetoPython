import time

numeros = []


def realizar_acao():
	texto = input("Digite um número: ").lower()

	try:
		numero = int(texto)
		numeros.append(numero)
	except:
		if texto == "sair":
			return texto
		elif texto == "somar":
			print(sum(numeros))
		elif texto == "limpar":
			numeros.clear()
			print("Calculadora reiniciada.")
		else:
			print("Digite um número válido.")


print("Esse programa corresponde a uma calculadora para somar números inteiros.")
print("Você pode digitar um número de cada vez e pressionar 'enter' para armazená-lo na calculadora.")
print("Quando quiser exibir a soma dos números, digite 'somar'.")
print("Quando quiser sair da calculadora, digite 'sair'.")
print("E se quiser limpar os números digitados, digite 'limpar'.")

while True:
	acao = realizar_acao()

	if acao == "sair":
		break

print("Aplicação será encerrada em 3 segundos.")
time.sleep(3)

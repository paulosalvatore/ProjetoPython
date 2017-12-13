def custo_hotel(noites):
	return noites * 140


def custo_aviao(cidade):
	custo = 0

	if cidade == "São Paulo":
		custo = 312.0
	elif cidade == "Porto Alegre":
		custo = 447.0
	elif cidade == "Recife":
		custo = 831.0
	elif cidade == "Manaus":
		custo = 986.0

	return custo


def custo_carro(dias):
	custo = dias * 40

	if dias >= 7:
		custo -= 50
	elif dias >= 3:
		custo = custo - 20

	return custo


def custo_total(noites, cidade, dias_carro, gasto_extra):
	return custo_hotel(noites) + custo_aviao(cidade) + custo_carro(dias_carro) + gasto_extra

noites = int(input("Quantas noitas você irá passar? "))
cidade = input("Para qual cidade você vai? ")
dias_carro = int(input("Quantos dias você usará o carro? "))
gasto_extra = int(input("Qual será o seu gasto extra?"))

custo = custo_total(noites, cidade, dias_carro, gasto_extra)

print("O custo total para ir para {}, ficar {} noites, usar o carro por {} dias e gastar R$ {:.2f} a mais é de R$ {:.2f}".format(cidade, noites, dias_carro, gasto_extra, custo))

precos = {
	"banana": 4,
	"maçã": 2,
	"laranja": 1.5,
	"pera": 3
}

estoques = {
	"banana": 6,
	"maçã": 0,
	"laranja": 32,
	"pera": 15
}


def computar_compra(mantimento):
	print("Sua compra foi realizada com sucesso.")
	total = 0
	for fruta in mantimento:
		estoque = estoques[fruta]
		if estoque > 0:
			print("Você comprou a fruta {}.".format(fruta))
			estoques[fruta] -= 1
			print("\tO novo estoque da fruta {} é de {}.".format(fruta, estoques[fruta]))
			preco = precos[fruta]
			print("\tVocê pagou R$ {:.2f} pela fruta {}.".format(preco, fruta))
			total += preco
		else:
			print("A fruta {} está indisponível em estoque.".format(fruta))
	print("Total das frutas: R$ {:.2f}".format(total))
	return total

mantimentos = []

frutas_disponiveis = list(precos.keys())
print("Frutas disponíveis:\n- {}".format("\n- ".join(frutas_disponiveis)))
print("Digite 'comprar' para realizar a compra.")

while True:
	comprar_fruta = input("Qual fruta você deseja comprar? ")

	if comprar_fruta == "comprar":
		computar_compra(mantimentos)
		break
	else:
		mantimentos.append(comprar_fruta)

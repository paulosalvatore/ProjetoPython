inventario = {
	"dinheiro": 500,
	"carteira": ["joia", "cartao", "caderno"],
	"mochila": ["faca", "blusa", "guarda-chuva", "garrafa"]
}


# Item 1

inventario["dinheiro"] += 50

print(inventario["dinheiro"])

# Item 2

inventario["carteira"].append("lenço")
print(inventario["carteira"])

# Item 3

inventario["mochila"].sort()
print(inventario["mochila"])

# Item 4

print(len(inventario["carteira"]))
print(len(inventario["mochila"]))

# Item 5

inventario["bolso"] = ["moeda", "papel"]
print(inventario["bolso"])

"""
Adicione R$ 50,00 ao elemento ‘dinheiro’ do inventário.
Adicione um novo item à carteira.
Ordene os itens da mochila por ordem alfabética.
Exiba na tela quantos itens a pessoa tem na carteira e na mochila.
Adicione uma nova lista ao inventário chamada ‘bolso’, e inclua alguns itens.
"""

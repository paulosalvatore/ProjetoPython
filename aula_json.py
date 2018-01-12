import json
import requests

link = "https://api.chucknorris.io/jokes/random"
conteudo = requests.get(link)
objeto = json.loads(conteudo.text)
piada = objeto["value"]
print(piada)

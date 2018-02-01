import requests
import json

url_base = "https://graph.facebook.com"
versao = 2.11
node = "me"
token = "EAACEdEose0cBAIbQl4Sgbrqcd9Ap3LbIwETZBOdKlKRZB4m9CfYOTnBwKZALnXkZBESlahqY6VY2qYB8gOwT6RaBo0x9DQMAmpvX2EPXvicRZC3fG9ftslZAUpTZCJtLpf2MR3PNR5mDzJXFuBgKLMdrJdp1TgcdmvG1oZA6El1PXqjxfhk0gXa5MGOBdZAPVCu9dBkg21x9bagZDZD"

campos = "id,name,friends.limit(20,40){name,email,birthday}"
before = "QVFIUnlGbUQ0ZA2NDS2MyeEpKbm1tUTFrMFFYM1NyNTYxYzhhU3NNc2VrdG1lYlRYZAVpVaHJnaGtnRFZAYSjhrQzU3VS1QaE00Qml3SlFBUTEtNU5xeGJhQ2p3"
campos += "&after=" + before

url = "{}/v{}/{}?fields={}&access_token={}".format(url_base, versao, node, campos, token)

print("url: {}".format(url))

conteudo = requests.get(url).text
objeto_json = json.loads(conteudo)

print(objeto_json)

print(objeto_json["friends"]["paging"]["cursors"]["after"])

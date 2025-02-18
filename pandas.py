import requests
import json
informacoes = '{"challenge_code": "AUTOMATE123"}'
requisicao  = requests.post("https://testte-c0443-default-rtdb.firebaseio.com/.json",data=informacoes)
print(requisicao)
print(requisicao.json())
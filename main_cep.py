import requests
from acesso_cep import BuscaEndereco

cep = 38408400
objeto_cep = BuscaEndereco(cep)

# r = requests.get("https://viacep.com.br/ws/38408400/json/")
# print(r.text)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro,cidade,uf)
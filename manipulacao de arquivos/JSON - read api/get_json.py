"""

Used API:

http://servicodados.ibge.gov.br/api/v1/publicacoes/{produto}

"""

import requests # make requests of web pages
import fileinput # manipule file inputs
import unicodedata # unicode convert data
import json # to manipule json files

produto = str(input("Digite uma palavra chave para buscar publicações: \n"))

try:
	filename = produto + "_pubs_ibge.json"

	request = requests.get("http://servicodados.ibge.gov.br/api/v1/publicacoes/{}".format(produto)) # request data from IBGE Publications API
	content = request.json()

	with open(filename, "w", encoding='utf8') as file: # with filename openned as file...
		json.dump(content, file, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

	print("Dados obtidos e arquivo criado!")

except:
	print("Erro ao obter dados e criar arquivo!")

"""

API usada:

https://servicodados.ibge.gov.br/api/v1/localidades/estados/{UF}

Tutoriais:

https://pyfpdf.readthedocs.io/en/latest/
https://github.com/reingart/pyfpdf
https://github.com/filipeaguilardeveloper/python-gerando-pdf

"""

import requests # biblioteca para requisicoes de paginas web
import wget # para dowload de arquivos web
from fpdf import FPDF # biblioteca para gerar e tratar arquivos PDF
import json

''' --------------------------------- OBTER DADOS DA API E GERAR ARQUIVO JSON --------------------------------- '''

unidade_federativa = input("Digite apenas a sigla da Unidade Federativa a qual se deseja obter os dados: ")
if len(unidade_federativa) != 2:
	print("UF inválida!")
	exit()

datalist = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/{}".format(unidade_federativa))
datalist = datalist.json()

def escrever_json(dados):
    with open("./data/distritos{}.json".format(unidade_federativa), "w", encoding='utf8') as arq:
        json.dump(dados, arq, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as arq:
        return json.load(arq)

escrever_json(datalist)
dados = ler_json("./data/distritos{}.json".format(unidade_federativa))

estado = dados["nome"]
regiao = dados["regiao"]["nome"]

#url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/{}".format(unidade_federativa)
#downloaded = wget.download(url)

''' --------------------------------- GERAR PDF --------------------------------- '''

pdf = FPDF() # classe para gerar pdf

def layoutPagina(arqPDF):
	arqPDF.set_xy(170, 3.5)
	arqPDF.image("./data/IBGE.png",  link='', type='', w=42, h=25) # adiciona imagem e define valores (argumentos) para os parametros

def defineTitulo(arqPDF):
	arqPDF.set_xy(90, 13)
	arqPDF.set_font("Times", 'B', 18) # seleciona fonte do titulo
	arqPDF.set_text_color(178, 34, 34)
	arqPDF.cell(50, 10, "Relatorio")

def inserirTexto(arqPDF):
	arqPDF.set_font("Arial", '', 16) # seleciona fonte do texto
	arqPDF.set_text_color(0, 0, 0)
	arqPDF.set_xy(35, 40)
	arqPDF.cell(70, 69, ("Região: %s" %(regiao)))
	arqPDF.set_xy(35, 48)
	arqPDF.cell(70 , 69, ("Estado: %s" %(estado)))


pdf.add_page() # adiciona pagina
layoutPagina(pdf)
defineTitulo(pdf)
inserirTexto(pdf)
pdf.output("./gen/relatorio.pdf", 'F') # cria arquivo com o que foi definido previamente

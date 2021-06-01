"""

OBJETOS = elemento computacional que representa alguma entidade (abstrata ou concreta)
CLASSES = estrutura que abstrai um conjunto de objetos com caracteristicas similares, define o comportamento de seus objetos - atraves de metodos - e os estados possiveis destes objetos - atraves de atributos

ATRIBUTOS = elementos que definem a estrutura de uma classe
INSTANCIAS = um objeto cujo comportamento e estado sao definidos pela classe
METODOS = funcao associada de uma classe

MENSAGEM = chamada a um objeto para invocar um de seus metodos
HERANCA = mecanismo que permite a uma subclasse extender uma superclasse aproveitado seus atributos e metodos herdados
POLIMORFISMO = propriedade de duas ou mais classes derivadas de uma mesma superclasse responderem a mesma mensagem, cada uma de uma forma diferente
ENCAPSULAMENTO = encapsular os dados de uma aplicacao significa evitar que estes sofram acessos indevidos. Para isso, e criada uma estrutura que contem metodos que podem ser utilizados por qualquer outra classe, sem causar inconsistências no desenvolvimento de um codigo

"""


''' isto e uma classe '''
class Livro(): # para receber parametros usa-se parenteses

	def __init__(self, isbn): # funcao (ou metodo, por estar dentro da classe) de inicaializacao - para inicializar cada objeto criado a partir desta classe
		# esses sao atributos (variaveis)
		self.nome = ""
		self.genero = "" # 'self' referencia cada atributo de um objeto criado a partir dessa classe
		self.ano = 0
		self.numpag = 0
		self.isbn = isbn

	def info(self): # metodos sao funcoes que recebem como parametro atributos do objeto criado
		print("LIVRO: %s \nGENERO: %s \nANO LANCA.: %s \nISBN: %s" %(self.nome, self.genero, self.ano, self.isbn)) # mostrar informacoes sobre objeto

	def __len__(self): # metodo especial
		return self.numpag



''' isto e um objeto (ou instancia da classe) '''
livro1 = Livro(9788594318725) # instanciando classe 'Livro()' ao criar objeto 'livro1' na classe e passando o valor do ISBN-13 para o parametro 'isbn'

livro1.ano = 1912
livro1.nome = "O Mundo Perdido" # definindo valores dos atributos do objeto
livro1.genero = "ficção/fantasia"
livro1.numpag = 240
print(str(type(livro1)))



''' isto e um metodo '''
livro1.info() # chamada do metodo criado
print("PAGINAS: " + str(len(livro1)) + '\n') # chamada do metodo especial 'len()'

if (hasattr(livro1, 'tipo_capa')): # verifica se tem atributo 'tipo_capa'
	print("Tem atributo de tipo de capa!")



''' isto e heranca '''
class Vertebrados(): # superclasse

	def __init__(self):
		self.coluna_vertebral = True
		self.num_patas = 0
		self.num_olhos = 0
		self.sistema_nervoso = True
		self.sistema_respiratorio = True

	def info(self):
		print("Classe que corresponde aos animais vertebrads, do filo 'chordata'.\n")


class Cachorro(Vertebrados): # subclasse

	def __init__(self):
		Vertebrados.__init__(self) # iniciando atributos e metodos da classe 'Vertebrados'
		self.pelos = True
		self.num_olhos = 2
		self.num_patas = 4
		self.familia = "canidae"

	def latir(self):
		print("Woolf!\n")


husky = Cachorro()
husky.__delattr__("sistema_nervoso") # metodo especial para deletar atributo 'sistema_nervoso' do objeto 'husky'
del husky.sistema_respiratorio # funcao que chama o metodo '__delattr__'

if (husky.coluna_vertebral == True): # o atributo coluna vertebral e uma heranca da classe 'Vertebrados'
	print("Cachorro é um animal vertebrado que pertence à família '{}' e que possui %s olhos e %s patas.".format(husky.familia) %(husky.num_olhos, husky.num_patas)) # em caso de conflitos entre metodos ou atributos, sao usados os da classe mais especifica
husky.latir() # isso e uma mensagem (ou chamada de metodo)



''' isto e polimorfismo '''
class FormaGeometrica(): # superclasse
	def calc_area(self):
		return "Erro no cálculo da área!"

class Quadrado(FormaGeometrica): # subclasse

	def __init__(self, base):
		self.base = base

	def calc_area(self):
		return self.base * self.base


class Circulo(FormaGeometrica): # subclasse

	def __init__(self, raio):
		self.raio = raio

	def calc_area(self):
		return self.raio * self.raio * 3.14

forma1 = Quadrado(5)
forma2 = Circulo(5)
print("Forma 1 é um quadrado de base %s e área %s. \nForma 2 é um círculo de raio %s e área %s.\n" %(5, forma1.calc_area(), 5, forma2.calc_area()))



''' isto e encapsulamento '''
class InfoFracamentePrivada(): # exemplo de classe com itens fracamente privados
	def __init__(self):
		self._idade = 25
 
	def _privmetod(self):
		print("método fracamente privado")

p1 = InfoFracamentePrivada()
print(p1._idade)
p1._privmetod()


class InfoFortementePrivada(): # exemplo de classe com itens fortemente privados
	def __init__(self):
		self.__senha = 147256
 
	def __privmetod(self):
		print("método fortemente privado")

p2 = InfoFortementePrivada()
#print(p2.__senha) mensagem retornando erro, pois o atributo e fortemente privado
print(p2._InfoFortementePrivada__senha) # agora deu certo
#p2.__privmetod() mensagem retornando erro, pois o metodo e fortemente privado
p2._InfoFortementePrivada__privmetod()

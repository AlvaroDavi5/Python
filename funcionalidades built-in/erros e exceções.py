# se não houver erro em alguma parte do bloco try o bloco except não será executado
try:
	print("Bloco sem erros")
except:
	print("Ocorreu um erro ou exceção")

# se houver erro em alguma parte do bloco try o bloco except será executado
try:
	print(varVazia)
	print("Bloco sem erros")
except:
	print("Ocorreu um erro ou exceção")




try:
	5 + 'a'
except TypeError:
	print("Não é permitida a soma entre tipo inteiro e caractere/string")

try:
	open("arquivoInexistente.txt", 'r')
except FileNotFoundError:
	print("Parece que esse arquivo não existe")

tupla = (1, 2, 3)
try:
	tupla.append(4)
except SyntaxError:
	print("Parece que alguma parte do seu código está incorreta")
except AttributeError:
	print("O objeto tupla não possui o atributo append")
else:
	print("Sem erros")

try:
	12 / 0
except ArithmeticError:
	print("Não existe divisão por zero")
finally:
	print("Encerrando programa")
	exit()

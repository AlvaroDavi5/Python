# Calculadora em Python

import math


def adicao():
	num1 = int(input("Digite o somando:\n"))
	num2 = int(input("Digite o somado:\n"))
	res = num1 + num2
	print("%s + %s = %s \n" %(num1, num2, res))

def subtracao():
	num1 = int(input("Digite o subtraendo:\n"))
	num2 = int(input("Digite o subtraído:\n"))
	res = num1 - num2
	print("%s - %s = %s \n" %(num1, num2, res))

def multiplicacao():
	num1 = int(input("Digite o multiplicando:\n"))
	num2 = int(input("Digite o multiplicador:\n"))
	res = num1 * num2
	print("%s * %s = %s \n" %(num1, num2, res))

def divisao():
	num1 = int(input("Digite o dividendo:\n"))
	num2 = int(input("Digite o divisor:\n"))
	res = num1 / num2
	print("%s / %s = %s \n" %(num1, num2, res))

def potencicacao():
	num1 = int(input("Digite o numero:\n"))
	num2 = int(input("Digite o expoente:\n"))
	res = num1 ** num2
	print("%s^%s = %s \n" %(num1, num2, res))

def radiciacao():
	num = int(input("Digite o quadrado:\n"))
	res = math.sqrt(num)
	print("raiz(%s) = %s \n" %(num, res))


# main
print("\n******************* Python Calculator *******************\n")

print("1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Potenciação \n6 - Radiciação")

opcao = int(input('Escolha uma das opções acima de acordo com o número correspondente: '))

if opcao == 1:
	adicao()
elif opcao == 2:
	subtracao()
elif opcao == 3:
	multiplicacao()
elif opcao == 4:
	divisao()
elif opcao == 5:
	potencicacao()
elif opcao == 6:
	radiciacao()
else:
	print("Operação inválida")
	exit

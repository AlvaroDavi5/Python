from math import sqrt # funcao sqrt() importada da biblioteca math

def potenciacao(num, expo): # definição de função
	i = 0
	res = num
	if expo < 0:
		return "FUNÇÃO APENAS PARA POTENCIAÇÃO"
	elif expo == 0:
		return 1
	else:
		while i < expo-1:
			res *= num
			i += 1
		return res



# função principal

numero = int(input("digite um número: "))
potencia = int(input("digite um expoente: "))
result = potenciacao(numero, potencia)
print("Resultado: %s \n" %(result))

quadrado = int(input("Digite o quadrado de um número: "))
raiz = sqrt(quadrado)
num = lambda root: root**2 # função lambda
print("Raiz quadrada de %s é: %s. \nPois %s² = %s\n" %(quadrado, raiz, raiz, num(raiz)))

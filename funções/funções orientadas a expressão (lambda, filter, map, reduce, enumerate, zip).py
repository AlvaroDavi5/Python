from functools import reduce

def soma(A, B):
	return A + B

def ehPar(num):
	if (num % 2 == 0):
		return True
	else:
		return False

def fahrenheit(num):
	return ((9.00 / 5.00) * num + 32)

listaC = [30, 45, 100, 0, 27, -12]

valores = [4, 5, 9, 0, 2, 7, 3, 1]





# função lambda
ao_cubo = lambda num: num**3


# função map
convertCelsToFah = map(fahrenheit, listaC)


# função reduce
valorGeral = reduce(soma, valores[1:])


# função filter
valoresPares = filter(ehPar, valores)


# função list comprehension
listaM = [c.upper() for c in "Ola mundo"]


# função zip
agrupaElementos = zip([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7])


# função enumerate
indiceValor = enumerate([1, 2, 3, 4, 5, 6])





doisAoCubo = ao_cubo(2)
print(doisAoCubo)
listaF = list(convertCelsToFah)
print(listaF)
print(valorGeral)
pares = list(valoresPares)
print(pares)
print(listaM)
agrupaElementos = tuple(agrupaElementos)
print(agrupaElementos)
print(list(indiceValor))

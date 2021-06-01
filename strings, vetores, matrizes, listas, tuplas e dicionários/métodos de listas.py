listanomes = ["Leonardo", "Donatello", "Rafael", "Michelangelo"]
print(listanomes)

listanomes.append("Dante") # adiciona ao fim da lista
print(listanomes)

listanomes.remove("Dante") # remove primeira ocorrencia do elemento na lista
print(listanomes)

listanomes.insert(5, "Darwin") # insere elemento em uma posição
print(listanomes)
listanomes.insert(7, "Tesla")
print(listanomes)

verifDante = listanomes.count("Dante") # conta ocorrências de um elemento na lista
if verifDante == 0:
	print("Dante não está na lista")
else:
	print("Dante aparece %s vezes nessa lista" %(verifDante))

listanomes.sort() # ordena elementos
print(listanomes)

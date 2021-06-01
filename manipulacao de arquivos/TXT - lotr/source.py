arq1 = open('./Linguagem Python/manipulacao de arquivos/textoOHobbit.txt', 'r') # arquivo aberto em modo leitura

print(arq1.read()) # lendo conteudo do arquivo
print(arq1.tell()) # contando quantidade de caracteres do arquivo
print(arq1.read(35)) # lendo apenas os primeiros 35 caracteres
print(arq1.seek(35,0)) # retornar para a posicao 35 do arquivo
print(arq1.read()) # lendo a partir do caractere 35




arq2 = open('/home/alvaro/Álvaro Davi/Programação/Linguagem Python/manipulacao de arquivos/discursoReiTheoden.txt', 'w') # arquivo aberto em modo escrita

arq2.write("[...] Podem ir, e não tenham medo.\nCavalguem cavaleiros de Théoden, cavalguem para a ruína e para a morte!\nLanças serão usadas, escudos serão partidos. Um dia de espada, um dia vermelho antes que o sol nasça.\nMOOORTEE!!!") # escrevendo conteudo no arquivo
arq2.close() # fechado antes de ler para evitar erros entre funcoes de escrita/leitura

arq2 = open('/home/alvaro/Álvaro Davi/Programação/Linguagem Python/manipulacao de arquivos/discursoReiTheoden.txt', 'r')
print(arq2.read())
print("\n")




arq3 = open('/home/alvaro/Álvaro Davi/Programação/Linguagem Python/manipulacao de arquivos/poemaInicialLOTR.txt', 'a') # arquivo aberto em modo append

sentenca1 = "Três anéis aos elfos, reis sob este céu,\n"
sentenca2 = "Sete aos senhores anões, em seus rochosos recintos,\n"
sentenca3 = "Nove aos homens, a quem a morte escolheu\n"
sentenca4 = "E Um anel ao Senhor do Escuro em sem escuro trono.\n"
sentenca5 = "Um Anel para a todos governar, Um anel para atraí-los e na escuridão aprisionar\n"
sentenca6 = "Na terra de Mordor onde as sombras recaem."

arq3.write(sentenca1)
arq3.write(sentenca2)
arq3.write(sentenca3)
arq3.write(sentenca4)
arq3.write(sentenca5)
arq3.write(sentenca6)
arq3.close()

arq3 = open('/home/alvaro/Álvaro Davi/Programação/Linguagem Python/manipulacao de arquivos/poemaInicialLOTR.txt', 'r')
print(arq3.read())

import os
import sqlite3
import pandas

if os.path.exists('dados.db'):
	os.remove('dados.db')

connection = sqlite3.connect('dados.db') # conexao com o SQLite aberta
cursor = connection.cursor() # cursor para navegar pela conexao

cursor.execute("CREATE TABLE IF NOT EXISTS pessoas" + # cria tabela "pessoas"
			   "(rg INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome VARCHAR(50), idade INTEGER, endereco TEXT)" # o RG e chave primaria e nao nula
)


cursor.execute("INSERT INTO pessoas (rg) VALUES (303789)")
cursor.execute("INSERT INTO pessoas (rg) VALUES (345435)")
cursor.execute("INSERT INTO pessoas (rg) VALUES (896878)")

df = pandas.read_sql(sql='SELECT * FROM pessoas', con=connection)
print(df)
print()


cursor.execute("UPDATE pessoas SET endereco = ''")
cursor.execute("UPDATE pessoas SET nome = 'fulano'")
cursor.execute("UPDATE pessoas SET nome = 'sicrano' WHERE rg = 345435")

df = pandas.read_sql(sql='SELECT * FROM pessoas', con=connection)
print(df)
print()


cursor.execute("UPDATE pessoas SET nome = 'Alvaro Davi', idade = 18, endereco = 'rua do silencio' WHERE rg = 303789")
cursor.execute("UPDATE pessoas SET nome = 'Matha Jones', idade = 28, endereco = 'alameda dos anjos' WHERE rg = 345435")
cursor.execute("UPDATE pessoas SET nome = 'Jack Harkness', idade = 5000, endereco = 'peninsula de Boeshire' WHERE rg = 896878")

df = pandas.read_sql(sql='SELECT * FROM pessoas', con=connection)
print(df)
print()

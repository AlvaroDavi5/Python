import os
from datetime import datetime
import time
import random
import sqlite3
import matplotlib.pyplot as plt
#%matplotlib notebook	para excutar dentro do Jupyter Notebook

def createTable(cursor):
	cursor.execute(
		"CREATE TABLE IF NOT EXISTS produtos" \
		"(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, prod_name TEXT, value REAL)"
	)

def dataInsert(cursor, connection):
	cursor.execute("INSERT INTO produtos VALUES(10, '2018-05-02 14:32:12', 'Teclado', 90)")
	connection.commit()

def data_insert_var(cursor, connection):
	new_date = datetime.now()
	new_prod_name = 'Placa de Vídeo'
	new_value = random.randrange(300, 900)
	cursor.execute("INSERT INTO produtos (date, prod_name, value) VALUES (?, ?, ?)", (new_date, new_prod_name, new_value))
	connection.commit()

def read_all_data(cursor):
	cursor.execute("SELECT * FROM produtos")
	for row in cursor.fetchall():
		print(row)

def read_specific_data(cursor):
	cursor.execute("SELECT * FROM produtos WHERE value > 400.00")
	for row in cursor.fetchall():
		print(row)

def read_specific_column(col_num, cursor):
	cursor.execute("SELECT * FROM produtos")
	for row in cursor.fetchall():
		print(row[col_num])

def update_value(cursor, connection):
	cursor.execute("UPDATE produtos SET value = 500.50 WHERE value < 400.00")
	connection.commit()

def graphic_plot(cursor):
	cursor.execute("SELECT id, value FROM produtos")
	ids = []
	values = []
	data = cursor.fetchall()
	for row in data:
		ids.append(row[0])
		values.append(row[1])
	plt.bar(ids, values) # criar grafico de barras com os dados
	plt.show() # plotar grafico

def main():
	os.remove("dsa.db") if os.path.exists("dsa.db") else None # remove dsa.db se existir, se nao, nao faz nada

	conn = sqlite3.connect("dsa.db")
	c = conn.cursor()

	createTable(c)

	dataInsert(c, conn)
	for i in range(5):
		data_insert_var(c, conn)

	print("\nTodos os Produtos:\n")
	read_all_data(c)
	print("\nProdutos Acima de R$ 400,00:\n")
	read_specific_data(c)
	print("\nTipos de Produtos:\n")
	read_specific_column(2, c)
	update_value(c, conn)
	read_specific_data(c)
	graphic_plot(c)

	c.close()
	conn.close()


if __name__ == '__main__':
	main()

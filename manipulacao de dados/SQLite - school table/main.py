import os
import sqlite3 # import SQLite library

# remove file if it exists
if os.path.exists("./escola.db"):
	os.remove("./escola.db")
else:
	None

# make connection with database, if database not exists, build database
con = sqlite3.connect("escola.db")

# cursor to navigate to all registers on database
cur = con.cursor()

# SQL instruction (DDL)
sql_create_table = "create table cursos "\
"(id integer primary key, "\
"titulo varchar(100), "\
"nota_mec integer, "\
"centro_ensino varchar(140))" # unnecessary parse to uppercase

cur.execute(sql_create_table) # the cursos navigate in the SQL instruction and execute it

# SQL instruction (DML)
sql_insert_data = "insert into cursos values (?, ?, ?, ?)"

recset = [
	(1045, "Engenharia da Computacao", 5, "Centro Tecnologico"), 
	(1018, "Direito", 5, "Centro de Ciencias Juridicas e Economicas"), 
	(1024, "Matematica", 4, "Centro de Ciencias Exatas")
] # to register an list of 3 tuples with 4 elements each

for rec in recset:
	cur.execute(sql_insert_data, rec) # registering

# make commit on connection to record data transaction
con.commit()

# verify if data are recorded
sql_select_all = "select * from cursos"
cur.execute(sql_select_all)
dataset = cur.fetchall()
for data in dataset:
	print("Id: %d \nCurso: %s \nNota do MEC: %d \nCentro de Ensino: %s" %(data))
	print()

con.close() # closing connection

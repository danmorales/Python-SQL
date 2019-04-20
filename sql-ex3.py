import sqlite3
import pandas as pd

conn = sqlite3.connect('Dados.sqlite')

cursor = conn.cursor()

tabelas = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print("Tabelas")
print(tabelas)

print("Colunas da tabela A")
colunasA = cursor.execute("PRAGMA table_info('TabelaA') ").fetchall()
print(colunasA)
print("\n")	
print("Colunas da tabela B")
colunasB = cursor.execute("PRAGMA table_info('TabelaB') ").fetchall()
print(colunasB)

cursor.execute("SELECT COUNT(*) FROM TabelaA;")
countA = cursor.fetchall()
print("\n")	
print('\nTotal de linhas Tabela A: {}'.format(countA[0][0]))

print("\n")	

cursor.execute("SELECT COUNT(*) FROM TabelaB;")
countB = cursor.fetchall()
print("\n")	
print('\nTotal de linhas Tabela B: {}'.format(countB[0][0]))

print("\n")	

rowsA = cursor.execute("SELECT * FROM TabelaA;").fetchall()
if rowsA == []:
	print("Tabela vazia")
else:
	for row in rowsA:
		print("ID: ",row[0]," A: ",row[1]," NUMERO: ",row[2])
	
print("\n")		
		
rowsB = cursor.execute("SELECT * FROM TabelaB;").fetchall()
if rowsB == []:
	print("Tabela vazia")
else:
	for row in rowsB:
		print("ID: ",row[0]," B: ",row[1]," CODIGO: ",row[2])
		
print("\n")		

innerjoin = cursor.execute("SELECT TabelaA.ID, A, NUMERO, TabelaB.ID, B, CODIGO FROM TabelaA INNER JOIN TabelaB ON TabelaB.ID = TabelaA.ID").fetchall()

print("Inner join")
for row in innerjoin:
	print(row)
	
print("\n")		

leftjoin = cursor.execute("SELECT TabelaA.ID, A, NUMERO, TabelaB.ID, B, CODIGO FROM TabelaA LEFT JOIN TabelaB ON TabelaB.ID = TabelaA.ID").fetchall()

print("Left join")
for row in leftjoin:
	print(row)
	
print("\n")		

crossjoin = cursor.execute("SELECT TabelaA.ID, A, NUMERO, TabelaB.ID, B, CODIGO FROM TabelaA CROSS JOIN TabelaB ON TabelaB.ID = TabelaA.ID").fetchall()

print("CROSS join")
for row in crossjoin:
	print(row)

cursor.close()
conn.commit()
conn.close()


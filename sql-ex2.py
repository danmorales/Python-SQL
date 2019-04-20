import sqlite3

conn = sqlite3.connect('Funcionarios.sqlite')

cursor = conn.cursor()

tabelas = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print("Tabelas")
print(tabelas)

print("\n")
print("Exibindo dados da tabela")

cursor.execute("SELECT COUNT(*) FROM FUNCIONARIOS;")
count = cursor.fetchall()
print("\n")	
print('\nTotal de linhas: {}'.format(count[0][0]))

rows = cursor.execute("SELECT * FROM FUNCIONARIOS;").fetchall()
if rows == []:
	print("Tabela vazia")
else:
	for row in rows:
		print("ID: ",row[0]," NOME: ",row[1]," IDADE: ",row[2]," CARGO: ",row[3]," SALARIO: R$",row[4])

print("\n")	
print("Atualizando funcionário com ID=1")
conn.execute("UPDATE FUNCIONARIOS set SALARIO = 8000 where ID = 1")
conn.commit()

print("\n")
print("Tabela atualizada")
rows = cursor.execute("SELECT * FROM FUNCIONARIOS;").fetchall()
if rows == []:
	print("Tabela vazia")
else:
	for row in rows:
		print("ID: ",row[0]," NOME: ",row[1]," IDADE: ",row[2]," CARGO: ",row[3]," SALARIO: R$",row[4])

print("\n")
print("Removendo funcionário com ID=5")
conn.execute("DELETE from  FUNCIONARIOS where ID = 5")
conn.commit()

print("\n")
print("Tabela atualizada")
rows = cursor.execute("SELECT * FROM FUNCIONARIOS;").fetchall()
if rows == []:
	print("Tabela vazia")
else:
	for row in rows:
		print("ID: ",row[0]," NOME: ",row[1]," IDADE: ",row[2]," CARGO: ",row[3]," SALARIO: R$",row[4])
		
print("\n")
print("Selecionando funcionários com salário superior a R$5,000")

minsal = cursor.execute("SELECT * FROM FUNCIONARIOS WHERE SALARIO >= 5000;").fetchall()
for row in minsal:
		print("ID: ",row[0]," NOME: ",row[1]," IDADE: ",row[2]," CARGO: ",row[3]," SALARIO: R$",row[4])

print("\n")
print("Ordenando por salário")
salario = cursor.execute("SELECT * FROM FUNCIONARIOS ORDER BY SALARIO ASC;").fetchall()
for row in salario:
		print("ID: ",row[0]," NOME: ",row[1]," IDADE: ",row[2]," CARGO: ",row[3]," SALARIO: R$",row[4])

print("\n")
print("Ordenando por salário e idade")
salario2 = cursor.execute("SELECT * FROM FUNCIONARIOS ORDER BY SALARIO ASC, IDADE ASC;").fetchall()
for row in salario2:
		print("ID: ",row[0]," NOME: ",row[1]," IDADE: ",row[2]," CARGO: ",row[3]," SALARIO: R$",row[4])
		
print("\n")
print("Exibindo os dois maiores salários")
salario3 = cursor.execute("SELECT * FROM FUNCIONARIOS ORDER BY SALARIO DESC LIMIT 2;").fetchall()
for row in salario3:
		print("ID: ",row[0]," NOME: ",row[1]," IDADE: ",row[2]," CARGO: ",row[3]," SALARIO: R$",row[4])
		
print("\n")
print("Exibindo salários entre R$4,000 e R$8,000 e ordenando por salário")
salario4 = cursor.execute("SELECT * FROM FUNCIONARIOS WHERE SALARIO BETWEEN 4000 AND 8000 ORDER BY SALARIO ASC;").fetchall()
for row in salario4:
		print("ID: ",row[0]," NOME: ",row[1]," IDADE: ",row[2]," CARGO: ",row[3]," SALARIO: R$",row[4])
		
print("\n")
print("Exibindo funcioários com ID=1 ou ID=3")
salario5 = cursor.execute("SELECT * FROM FUNCIONARIOS WHERE ID IN (1,3);").fetchall()
for row in salario5:
		print("ID: ",row[0]," NOME: ",row[1]," IDADE: ",row[2]," CARGO: ",row[3]," SALARIO: R$",row[4])

print("\n")
print("Exibindo funcioários com IDs diferentes de 1, 3 e 5")
salario6 = cursor.execute("SELECT * FROM FUNCIONARIOS WHERE ID NOT IN (1,3,5);").fetchall()
for row in salario6:
		print("ID: ",row[0]," NOME: ",row[1]," IDADE: ",row[2]," CARGO: ",row[3]," SALARIO: R$",row[4])

print("\n")
print("Exibindo nomes iniciados com a letra A")
nome = cursor.execute("SELECT * FROM FUNCIONARIOS WHERE NOME LIKE 'A%';").fetchall()
for row in nome:
		print("ID: ",row[0]," NOME: ",row[1]," IDADE: ",row[2]," CARGO: ",row[3]," SALARIO: R$",row[4])

print("\n")
print("Exibindo nomes que contenham a letra O")
nome2 = cursor.execute("SELECT * FROM FUNCIONARIOS WHERE NOME LIKE '%o%';").fetchall()
for row in nome2:
		print("ID: ",row[0]," NOME: ",row[1]," IDADE: ",row[2]," CARGO: ",row[3]," SALARIO: R$",row[4])

cursor.close()
conn.commit()
conn.close()
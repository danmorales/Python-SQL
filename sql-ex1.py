import sqlite3

def cria_tabela():
	cursor.execute('''CREATE TABLE CLIENTES
         (ID INT PRIMARY KEY     NOT NULL,
         NOME           TEXT    NOT NULL,
         IDADE            INT     NOT NULL,
         ENDERECO        CHAR(50),
         CEP          CHAR(9));''')

def ler_tabela():
	rows = cursor.execute("SELECT * FROM CLIENTES;").fetchall()
	if rows == []:
		print("Tabela vazia")
		return False
	else:
		for row in rows:
			print("ID: ",row[0]," NOME: ",row[1]," IDADE: ",row[2]," ENDERECO ",row[3]," CEP ",row[4])
		return True

conn = sqlite3.connect('Clientes.sqlite')

cursor = conn.cursor()

print("Banco de dados criado com sucesso")

print("\n")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

if tabelas != []:
	print("\n")
	print("Exibindo tabelas")
	print(tabelas)

tabela = 'CLIENTES'
leitura = True

if tabelas == []:
	print("\n")
	print("Banco de dados sem tabelas")
	print("Criando tabela ",tabela)
	cria_tabela()
elif tabela in tabelas[0]:
	print("\n")
	print("Tabela ",tabela, " existe")
	print("Lendo tabela")
	leitura = ler_tabela()
else:
	print("\n")
	print("Criando tabela ",tabela)
	cria_tabela()

if leitura == False:
	print("Adicionando elemento a tabela")
	cursor.execute("INSERT INTO CLIENTES (ID,NOME,IDADE,ENDERECO,CEP) \
      VALUES (1, 'User', 30, 'Rua ABC 12', '01234-000')");


cursor.close()
conn.commit()
conn.close()
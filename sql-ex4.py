import pandas as pd
import sqlite3

conn = sqlite3.connect('Funcionarios.sqlite')

df = pd.read_sql_query("SELECT * FROM FUNCIONARIOS;", conn)

print(df)

comissao = [5,12,3,6,2,14,12,18,20,5,12,7,12,10]

df['COMISSAO'] = comissao

print("\n")	
print(df)

conn2 = sqlite3.connect('Funcionarios_new.sqlite')

df.to_sql("FUNCIONARIOS", conn2, if_exists="replace")


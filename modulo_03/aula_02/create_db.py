# importa a biblioteca do SQLite
import sqlite3

# Conecta ao banco de dados (o arquivo 'banco.db' será criado se não existir)
conn = sqlite3.connect("banco.db")

# Fecha a conexão para finalizar
conn.close()

print("Banco de dados 'banco.db' criado com sucesso!")

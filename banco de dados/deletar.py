import sqlite3     

#conexão e criação da tabela
conexao = sqlite3.connect('departamento.db')

tabela = """
CREATE TABLE IF NOT EXISTS funcionario (
    codigo  INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)

);
"""

consulta = conexao.cursor()

consulta.execute(tabela)

#solicitar código para deletar
codigo = int(input("Qual o codigo do funcionário : "))

sql =  "DELETE FROM funcionario WHERE codigo = ?"

campos = (codigo,)#É preciso colocar uma círgula do depois do item para configurar que temos uma tupla("lista"), caso contrário não será aceita como uma tupla válida. Isso é feito quando temos apenas um valor para substituir

consulta.execute(sql, campos)

conexao.commit()

print(consulta.rowcount, "Uma linha deletada com sucesso\n")
conexao.close()
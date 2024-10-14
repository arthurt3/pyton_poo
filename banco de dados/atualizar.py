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

#solicitar campos para atualizar 
nome = input("Informe o novo nome do funcionário: ")
codigo = int(input("Qual o codigo do funcionário : "))

sql =  "UPDATE funcionario SET nome = ? WHERE codigo = ?"
campos = (nome, codigo)

consulta.execute(sql, campos)

conexao.commit()

print(consulta.rowcount, "Linha(s) atualizadas com sucesso\n")
conexao.close()
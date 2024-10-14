import sqlite3
class Funcionario:
    def conexao(self):
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

        return conexao
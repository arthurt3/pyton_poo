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
    
    def inserir(self , nome, salario, cargo):
        conexao =  self.conexao()#Estamos chamando método 'conexão' que irá conectar com o banco
        sql = "INSERT INTO funcionario VALUES(?,?,?,?)"

        campos =  (None, nome, salario, cargo)

        consulta = conexao.cursor()
        consulta.execute(sql, campos)

        conexao.commit()
        print(consulta.rowcount,  "Registro inserido com sucesso!\n")
        conexao.close()

    def consultar (self):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql = "SELECT * FROM funcionario"
        consulta.execute(sql)
        resultado = consulta.fetchall()#pegando  todos os dados da tabela

        for item  in resultado:
            print(f"Codigo: {item[0]}")
            print(f"Nome: {item[1]}")
            print(f"Salário: {item[2]}")
            print(f"Cargo: {item[3]}")

        conexao.close()




        





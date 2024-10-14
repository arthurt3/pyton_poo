import sqlite3 #importando uma biblioteca de banco de dados

#Passo 1 - Estabelecendo conexão com o banco
conexao = sqlite3.connect('departamento.db') #nome do banco de dados, e o arquivo que irá  armazenar o banco de dados

#Passo 2 - Verificar se a tabela existe ou não
tabela = """
CREATE TABLE IF NOT EXISTS funcionario (
    codigo  INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)

);"""

#Passo 3 - Acessar objeto da biblioteca sqlite 3 para manipular o banco 
consulta  = conexao.cursor() # O obejto  cursor é usado para executar SQL commands

#Passo 4 - Executar  o comando de criação da tabela
consulta.execute(tabela)

#Passo 5 - solicitar dados da tabela 
nome = input("Informe o nome  do funcionário: ")
salario = float(input("Informe o salário do funcionário: "))
cargo = input("Informe o cargo do funcionário: ")

#Passo  6 - Criando comando para Inserir dados na tabela
sql = "INSERT  INTO funcionario  VALUES (?,?,?,?)"# colocamos ? no lugar do dados reais, para  evitar a injeção de dados de ataques de  sql injection.

#Passo 7 - Organizar os dados substituídos a ? com os dados reais
campos = (None, nome, salario, cargo ) #None é usado para o código, pois ele é autoincremento, criando uma tupla  com os dados reais que serão trocados pela ?

#Passo 8 - Executar o comamdo sql e substituir ? pelos campos

consulta.execute(sql, campos)

#Passo 9 -  Salvar os dados no banco de dados
conexao.commit()

print(consulta.rowcount, "linha(s) foram inseridas com sucesso") #rowcount é usado para verificar a quantidade de linhas que foram inseridas

#Passo 10 - finalizar conexão 
conexao.close()



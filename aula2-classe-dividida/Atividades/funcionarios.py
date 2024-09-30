class Funcionarios:
    #Criando o método construtor
    def __init__(self, nome, cargo, salario):
        # estamos criando os atributos da classe utilizando o método  construtor. Nesse caso valores dos atributos.
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

#Criando os métodos normais
    def exibirDados(self):
        print(f"Olá {self.nome} seu cargo é {self. cargo} e seu salario é  {self.salario}")


    def verificarSalario (self):
        Salario = self.salario
        if self.salario <= 2000:
            print("Sem direito a bonus") 
        else: print("Você tem direito a bonus")
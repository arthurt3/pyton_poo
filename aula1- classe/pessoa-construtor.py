class Pessoa:
    #Criando o método construtor
    def __init__(self, nome, hobby, endereço):
        # estamos criando os atributos da classe utilizando o método  construtor. Nesse caso valores dos atributos.
        self.nome = nome
        self.hobby = hobby
        self.endereco = endereço

#Criando os métodos normais
def exibirDados(self):
    print(f"Olá {self.nome} seu hobby é {self.hobby} e seu endereço é  {self.endereço}")


#CRIANDO OS OBJETOS
pessoa1 = Pessoa( "João", "Futebol", "Rua 1, Nº 10")
pessoa1.exibirDados()# chamando o método de classe

pessoa2 =Pessoa( "Livia" , "Leitura", "Rua 2, Nº 20")
print(pessoa2.nome)

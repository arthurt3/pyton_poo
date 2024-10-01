class Conta:
    #Método Construtor
    def __init__(self,numero, titular, saldo, limite):
        #Quando colocamos 2 underlines ntes do nome do atrbuto indicammos que  ele é privado, o contrário significa  que ele é público


        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Criando os demais métodos
    def detalhes (self):
        print(f"Titular: {self.titular} seu saldo atual é  de R${self.saldo:.2f}")
        print(f"Seu limite é de R${self.limite:.2f}")
    #irá retornar o valor do limite
    def getLimite(self):
        return self.__limite
    #alterar o valor do limite
    def setLimite(self, valor):
        if valor < 0:
            print("Informe um valor positivo")
        else:
            self.__limite= valor
    
    #Criando metodo de depositar
    def depositar(self, valor):
        if  valor < 0:
            print("Informe um valor maior que zero")
        else:
            self.__saldo += valor
    #Criando metodo de sacar
    def sacar(self, valor):
        if self.__saldo <= 0 or valor  > self.__saldo:
            print("Você não tem saldo suficiente")
        else:
            self.__saldo -= valor
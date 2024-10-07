class funcionario:
    def __init__(self, cargo, salario=2000):
        self.__cargo = cargo
        self.__salario = salario #Esse atributo está opcional pois tem um valor default
    
    def getCargo(self):
        return self.__cargo
    
    def setCargo(self, novoCargo):
        self.__cargo= novoCargo

#iREMOS REALIZAR UMA FORMA UNICA DO PYTHON PARA ACESSAR ATRIBUTOS PRIVADOS
    #CRIANDO O "GET" DO SALÁRIO
    @property#ESSE ELEMENTO IRÁ CRIAR UM GET 'MAIS AMIGÁVEL'
    def salario(self):
        return self.__salario
    
    #CRIANDO O "SET" DO SALÁRIO
    @salario.setter#ESSE ELEMENTO IRÁ CRIAR UM SET 'MAIS amigável'
    def salario(self, valor):
        if valor <= 0:
            print("O valor do salário não pode ser menor ou igual a zero")
        else:
            self.__salario= valor

    
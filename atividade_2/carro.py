class Carro:
    def __init__(self,marca,modelo,ano,precoDiaria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.precoDiaria = precoDiaria
    
    def calcularPrecoAluguel(self):
        diasAluguel = int(input("Informe os dias de alugue: "))
        precoTotal = self.precoDiaria*diasAluguel
        print(f"Preço total:  {precoTotal}")
        
    def exibirDetalhes(self):
        print(f"A marca do carro é {self.marca} o modelo {self.modelo} é do ano {self.ano} e o preço da diaria: {self.precoDiaria}") 
    



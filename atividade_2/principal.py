
from carro import Carro

Carro1 = Carro("Fiat", "UNO", 2017,140)
Carro2 = Carro("Mercedes_Benz","T-80",1939,1000)

print("-"*50)

Carro1.exibirDetalhes()
Carro1.calcularPrecoAluguel()
print("-"*50)
Carro2.exibirDetalhes()
Carro2.calcularPrecoAluguel()
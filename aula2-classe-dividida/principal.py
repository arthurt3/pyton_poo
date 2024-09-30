#Estamos acessando o arquivo 'pessoa' e dentro do arquivo estamos importndo a classe 'Pessoa'
from pessoa import Pessoa

#Criando os objetos 
p1 = Pessoa( "Roberta", 20, "Hambúrguer")
p2 = Pessoa("Paulo", 25, "Pizza")

p1.mostrarComida()
p2.mostrarComida()

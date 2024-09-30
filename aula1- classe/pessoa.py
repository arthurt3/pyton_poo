class Pessoa:
    #Atributos 
    nome = "Fulano"
    idade = 25
    altura = 1.60

    #métodos - sãos os comportamentos da classe 
    def falar(self,texto):# self é um parametro obrigátorio do python que informa que o método pertence á própria classe que foi criada.
        print (f"Tenho algo pra te falar: {texto}")


#CRIANDO OBJETOS
pessoa1 = Pessoa()#desta forma estamos criando um objeto de tipo pessoa
 
print(pessoa1.nome, pessoa1.idade)
pessoa1.falar("Bom  dia, hoje é segunda-feira") 
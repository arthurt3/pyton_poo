class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    def descrever(self):
        print(f"O produto {self._nome} custa R${self._preco:.2f}")
    
    def calcularDesconto(self):
        pass

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome,preco)
        self.autor = autor
    
    def descrever(self):
        print(f"O livro {self._nome} foi escrito por  {self.autor} e custa R${self._preco:.2f}")

    def  calcularDesconto(self):
        desconto= self._preco * 0.1
        print(f"O livro {self._nome}  tem um desconto de R${desconto:.2f}, e custará {self._preco - desconto} ") 



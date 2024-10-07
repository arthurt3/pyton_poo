class Animal: #Superclasse ou classe-mãe
    def __init__(self, nome, idade):
        #Estamos mudando a visibilidade  do atributo de privado para protegido, dessa forma  podemos acessar o atributo fora da classe maãe, a parit das classes filhas
        self._nome = nome
        self._idade  = idade
    def exibirInfo (self):
        print(f"Nome: {self._nome}, Idade: {self._idade}")
    
    def exibirsom (self):
        som = input("Digite o som que o animal faz: ")
        print(f"O animal {self._nome} faz o som: {som}")

class mamifero(Animal):
    def alimetarFilhoetes (self):
        print(f"O mamífero: {self._nome} está alimentando seus filhotes.")

class reptil(Animal):
    def mudarPele(self):
        print(f"O reptil: {self._nome} está mudando a pele")
       
    
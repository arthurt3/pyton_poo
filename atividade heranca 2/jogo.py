class Personagem:
    def __init__(self, nome, vida =  5):

        self._nome  = nome
        self._vida = vida
    
    def atacar(self):
        print(f"O {self._nome } está atacando!")
    

class  Jogador(Personagem):
    def __init__(self, nome, raca, vida = 5):
        super().__init__(nome, vida)
        self._raca = raca
        self.lista =  []

    
    def Informacoes(self):
        print(f"Nome: {self._nome}, Raça: {self._raca}, Vida: {self._vida}" )

    def usarHabilidade(self,poder):
        print(f"O {self._nome} está usando a habilidade {poder}!")

    def coletarItem(self,item):
        self.lista.append(item)
        print(f"{item} coletado, itens no inventário : {self.lista}")
        
    
class Monstro(Personagem):
    def __init__(self, nome, tipo, forca, vida = 20 ):
        super().__init__(nome, vida)
        self._tipo = tipo
        self._forca = forca
    
    def exibirInformacoes(self):
        print(f"Nome: {self._nome}, Tipo: {self._tipo}, Vida: {self._vida}, Força: {self._forca}" )

    def invocarAliado(self, nomeAliado,  tipoAliado):
        print(f"{self._nome} está invocando o aliado {nomeAliado} do tipo {tipoAliado}")

    def defender (self):
        print(f"O {self._nome} está defendendo-se!")

        self._vida -= 1
        print(f"Vida do {self._nome}: {self._vida}")
            

        



        



    
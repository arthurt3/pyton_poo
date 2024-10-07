class Pessoa: #Superclasse ou classe-mãe
    def __init__(self, nome, cargo):
        #Estamos mudando a visibilidade  do atributo de privado para protegido, dessa forma  podemos acessar o atributo fora da classe maãe, a parit das classes filhas
        self._nome = nome
        self._cargo  = cargo
    def informacoes(self):
        print(f"{self._nome}, na empresa seu cargo  é: {self._cargo}")
    

#crindo a classe filha 
class Engenheiro(Pessoa): #Classe-filha ou subclass, esta herdando as carcterísticas da classe pessoa, que será sua clase mãe
    def mostraDetalhes(self):
        print("Olá, sou um engenheiro")


class Secretario (Pessoa):
    def relatorio(self):
        print(f"sou resposável pelas reuniões e meu cargo é : {self._cargo}")

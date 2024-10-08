from jogo import Personagem, Jogador, Monstro

pers1 = Personagem("Rakan")
pers1.atacar()

Jog1 = Jogador("Rakan",  "Elfo")
Jog1.Informacoes()
Jog1.usarHabilidade("Flecha Envenenada")
Jog1.coletarItem("Espada longa")
Jog1.coletarItem("Pedra do Poder")

mot1 =  Monstro("Vorath", "Demônio", 70,)
mot1.exibirInformacoes()
mot1.invocarAliado("Thundrax", "Dragão")
mot1.defender()
mot1.defender()
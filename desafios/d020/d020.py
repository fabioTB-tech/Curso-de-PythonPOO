from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogosFav = []
    
    def add_favoritos(self, *jogo):
        self.jogosFav.append(jogo)
    
    def ficha(self):

        ficha = Panel(f'Nome real: {self.nome}\nJogos favoritos:\n{self.jogosFav}', title=f'Jogador <{self.nick}>', expand=False)
        print(ficha)


j1 = Gamer('Ahri', 'Ahriri_Miau')
j1.add_favoritos('Celeste', 'Hollow Knigh', 'Forsaken')
j1.ficha()
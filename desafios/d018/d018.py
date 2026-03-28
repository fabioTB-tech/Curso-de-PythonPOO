from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo:str, quant:int, consumo:float = 0.4):
        self.titulo = titulo
        self.quant = quant
        self.consumo = consumo
        self.preco = 82.40
    
    def analisar(self):
        totConsumo = self.consumo * self.quant
        totPreco = self.preco * totConsumo
        divPreco = (totPreco / self.quant) if self.quant > 1 else self.preco
        analise = [
            f'Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]',
            f'Cada participante comerá {self.consumo}Kg e cada Kg custa {self.preco}',
            f'Recomendo [blue]comprar {totConsumo:.3f}Kg[/] de carne',
            f'O custo total será de [green]R${totPreco:,.2f}[/]',
            f'Cada pessoa pagará [yellow]R${divPreco:,.2f}[/] para participar.'
        ]
        tabela = Panel(f'{analise[0]}\n{analise[1]}\n{analise[2]}\n{analise[3]}\n{analise[4]}', title=self.titulo, width=80)
        print(tabela)


c1 = Churrasco('Churras dos Amigos', 100)
c1.analisar()
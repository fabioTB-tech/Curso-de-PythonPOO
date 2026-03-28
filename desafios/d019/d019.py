from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo:str, paginas:int = 5):
        self.titulo = titulo
        self.pag = paginas
        self.quantPag = []
        self.cont = 0
        for pag in range(1, self.pag+1):
            self.quantPag.append(f'Pág{pag}')
    
    def avancar_paginas(self, quant):
        newQuant = quant + self.cont
        while self.cont < newQuant:
            self.cont += 1
            if self.cont >= len(self.quantPag):
                quant = (len(self.quantPag) + quant) - (newQuant + 1)
                print(f'[blue]Você avançou {quant} {'páginas' if quant > 1 else 'página'} e agora está na[/] [yellow]página {self.quantPag.index(pagAtual)+1}[/]')
                print(f':closed_book: [red]Você chegou no final do livro "{self.titulo}"[/]')
                break
            pagAtual = self.quantPag[self.cont]
            print(pagAtual, end=' > ')
            sleep(0.5)
            if self.cont == newQuant:
                print(f'[blue]Você avançou {quant} {'páginas' if quant > 1 else 'página'} e agora está na[/] [yellow]página {self.quantPag.index(pagAtual)+1}[/]')

        


li = Livro('10 coisas que aprendi', 20)
li.avancar_paginas(5)
li.avancar_paginas(10)
li.avancar_paginas(110)
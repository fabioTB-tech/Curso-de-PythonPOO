from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo, emp='Curso em Vídeo'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = emp
    
    def apresentacao(self):
        return f':V: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}'


c1 = Funcionario('Maria', 'Administração', 'Diretora')
print(c1.apresentacao())

c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentacao())
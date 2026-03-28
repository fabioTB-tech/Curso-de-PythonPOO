# Declaração da classe
class Gafanhoto:
    # Atributos
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ''
        self.idade = 0

    # Métodos
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'


# Declaração dos objetos
g1 = Gafanhoto() # Instância

g1.nome = 'Ahri'
g1.idade = 18

print(g1.mensagem())

# --- --- --- --- --- ---

g2 = Gafanhoto()

g2.nome = 'Celeste'
g2.idade = 17

print(g2.mensagem())
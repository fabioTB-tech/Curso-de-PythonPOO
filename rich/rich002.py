from rich import print, inspect
from rich.panel import Panel

caixa = Panel("Esse aqui é um painel de exemplo", title='Mensagem', style='blue', width=37)

# inspect(Panel)
print(caixa)
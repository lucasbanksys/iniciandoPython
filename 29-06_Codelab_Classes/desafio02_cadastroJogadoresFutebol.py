class Jogadores:
    def __init__(self, nome, partidas, gols):
        self.nome = nome
        self.partidas = partidas
        self.gols = gols

    def MostrarDados(self):
        return f'''
Nome = {self.nome}
Partidas = {self.partidas}
Gols = {self.gols}   
'''

print("Aproveitamento dos jogadores:")

jogador1 = Jogadores("Cristiano Ronaldo", 3, 4)
jogador2 = Jogadores("Messi", 4, 5)

print(jogador1.MostrarDados())
print(jogador2.MostrarDados())
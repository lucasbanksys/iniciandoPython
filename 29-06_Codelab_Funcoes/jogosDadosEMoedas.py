from random import randint

class Jogos:
    def __init__(self, dados, moedas):
        self.dados = dados
        self.moedas = moedas

    def jogarDados(self):
        valorDado = randint(1,6)
        return valorDado

    def jogarMoeda(self):
        valorMoeda = randint(1,2)
        if valorMoeda == 1:
            return "cara"
        else: 
            return "coroa"
            
from random import randint
from time import sleep

escolha = 1

class Jogos:
    def __init__(self, escolhaJogo):
        self.escolhaJogo = escolhaJogo

    def Jogar(self):
        if self.escolhaJogo == 1:
            valorDado = randint(1,6)
            print(f"A face do dado caiu com valor: {valorDado}")
        elif self.escolhaJogo == 2:
            valorMoeda = randint(1,2)
            print("E o resultado foi...")
            sleep(1)
            if valorMoeda == 1:
                print("CARA!") 
            else: 
                print("COROA!")

while escolha != 0:        

    print('''
    Você deseja:
    1 - Jogar dados
    2 - Jogar moedas
    0 - Sair do jogo
    ''')

    escolha = Jogos(int(input("Sua opção: ")))

    escolha.Jogar()

    if escolha.escolhaJogo == 0:
        break
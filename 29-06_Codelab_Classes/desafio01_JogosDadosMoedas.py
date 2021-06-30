from desafio01_bibJogos import Jogos

escolha = 1

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
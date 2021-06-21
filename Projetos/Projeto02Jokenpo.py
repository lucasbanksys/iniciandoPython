from random import randint
from time import sleep

vitoriasUser = 0
vitoriasPC = 0
grandeVencedor = ""
parar = "N"
print("Bem vindo ao JOGO JOKENPÔ\n")

while parar != "S":

    qtdeRodadas = int(input("Quantas rodadas você deseja jogar? "))

    for i in range(qtdeRodadas):

        jogada = input("\nEscolha sua jogada: P(PEDRA), (L)PAPEL, (T)TESOURA: ").upper().strip()
        
        if jogada == "X":
            break

        jogadaPC = randint(1,3)

        if jogadaPC == 1:
            print("O computador escolheu PEDRA.")
        elif jogadaPC == 2:
            print("O computador escolheu PAPEL.")
        elif jogadaPC == 3:
            print("O computador escolheu TESOURA.")

        sleep(1)

        if jogada == "P" and jogadaPC == 1:
            print("Empatou!")
        elif jogada == "P" and jogadaPC == 2:
            print("O computador venceu! Papel contra pedra!")
            vitoriasPC += 1
        elif jogada == "P" and jogadaPC == 3:
            print("Você venceu! Pedra contra tesoura!")
            vitoriasUser += 1

        if jogada == "L" and jogadaPC == 2:
            print("Empatou!")
        elif jogada == "L" and jogadaPC == 3:
            print("O computador venceu! Tesoura contra papel!")
            vitoriasPC += 1
        elif jogada == "L" and jogadaPC == 1:
            print("Você venceu! Papel contra pedra!")
            vitoriasUser += 1

        if jogada == "T" and jogadaPC == 3:
            print("Empatou!")
        elif jogada == "T" and jogadaPC == 1:
            print("O computador venceu! Pedra contra tesoura!")
            vitoriasPC += 1
        elif jogada == "T" and jogadaPC == 2:
            print("Você venceu! Tesoura contra papel!")
            vitoriasUser += 1

        if vitoriasPC > vitoriasUser:
            grandeVencedor = "Computador"
        elif vitoriasPC < vitoriasUser:
            grandeVencedor = "Usuário"
        else:
            grandeVencedor = "Não houve um grande vencedor. Empate"

    parar = input("\nDeseja parar? [S/N]: ").upper().strip()[0]
    
    if parar == "S":
        break
    elif parar == "N": 
        continue
    else:
        print("Opção inválida.")

print(f"""
Você venceu {vitoriasUser} vez(es). O computador venceu {vitoriasPC} vez(es).
O grande vencedor foi: {grandeVencedor}!
""")
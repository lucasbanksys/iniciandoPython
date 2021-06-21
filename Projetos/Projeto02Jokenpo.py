from random import randint
from time import sleep

vitorias = 0
parar = "A"
print("Bem vindo ao JOGO JOKENPÔ\n")
print("Digite X para parar o jogo.\n")

while parar != "X":

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
    elif jogada == "P" and jogadaPC == 3:
        print("Você venceu! Pedra contra tesoura!")
        vitorias += 1

    if jogada == "L" and jogadaPC == 2:
        print("Empatou!")
    elif jogada == "L" and jogadaPC == 3:
        print("O computador venceu! Tesoura contra papel!")
    elif jogada == "L" and jogadaPC == 1:
        print("Você venceu! Papel contra pedra!")
        vitorias += 1

    if jogada == "T" and jogadaPC == 3:
        print("Empatou!")
    elif jogada == "T" and jogadaPC == 1:
        print("O computador venceu! Pedra contra tesoura!")
    elif jogada == "T" and jogadaPC == 2:
        print("Você venceu! Tesoura contra papel!")
        vitorias += 1

print(f"\n Você venceu {vitorias} vez(es).")
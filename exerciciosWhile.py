# # import random
# # import sleep from time

# sexo = str(input("Digite seu sexo [M/F]: ")).upper().strip()[0]

# while sexo not in "MF":
#     print("Sexo invalido. Tente novamente.")
#     sexo = str(input("Digite seu sexo [M/F]: "))

# print(f"\nO sexo digitado foi {sexo}.")

import random
from time import sleep

palpites = 1

print("\nOi, sou seu pc e vou pensar em um numero entre 0 e 15.\n")
sleep(2)
numeroPensado = random.randint(0,15)

numeroUsuario = int(input("Digite o numero que voce acha que eu pensei: "))

while numeroUsuario != numeroPensado:
    if numeroUsuario > numeroPensado:
        palpites += 1
        print("\nMenos... digite um numero menor.")
        numeroUsuario = int(input("Digite o numero que voce acha que eu pensei: "))
    elif numeroUsuario < numeroPensado:
        palpites += 1
        print("\nMais... digite um numero maior.")
        numeroUsuario = int(input("Digite o numero que voce acha que eu pensei: "))
print(f"\nMuito bem. Voce acertou o numero! Voce fez {palpites} palpite(s).")

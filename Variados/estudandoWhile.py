# for c in range(1,4):
#     n = int(input("Digite zero para finalizar: "))
# print(f"FIM {n}")
# -----------
# resp = ''
# while resp != 'S':
#     nome = str(input("Digite seu nome: "))
#     resp = str(input("Voce quer finalizar? [S/N]").strip().upper()[0])
#     if resp == "":
#         resp = str(input("Voce quer finalizar? [S/N]").strip().upper()[0])
# print("Fim")
# -------------------

# par = impar = 0
# n = 1

# while n != 0:
#     n = int(input('Digite um numero: '))
#     if n % 2 == 0:
#         par += 1
#     else:
#         impar += 1
# print(f"""
# Voce digitou {par} numero pares.
# E {impar} numeros impares.
# """)

print("A senha correta: 123456  \n")
senha = int(input("Digite sua senha: "))


while senha != 123456:
    print("Senha invalida. Tente novamente!")
    senha = int(input("Digite sua senha: "))
print("Usuario logado.")
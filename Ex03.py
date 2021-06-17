maiorIdade = 0
menorIdade = 0

for i in range(1,8):
    nascimento = int(input("Digite o ano de nascimento: "))
    idade = 2021 - nascimento
    if idade >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1

print(f"""
Das 7 pessoas inseridas sao:
{maiorIdade} maior de idade,
{menorIdade} menor de idade.
""")
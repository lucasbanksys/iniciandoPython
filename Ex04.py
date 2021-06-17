qtdeNumerosPares = 0
soma = 0

for i in range(0,6):
    numeroInteiro = int(input("Digite o numero inteiro: "))
    if numeroInteiro % 2 == 0:
        qtdeNumerosPares += 1
        soma += numeroInteiro
    else:
        continue

print(f"""
A soma dos números pares é: {soma}
A quantidade de númers pares digitados foi: {qtdeNumerosPares}
""")
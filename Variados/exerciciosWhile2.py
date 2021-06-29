peso = float(input("Digite o peso: "))
menor = maior = peso

for contador in range(1,5):
    peso = float(input("Digite o peso: "))
    if peso > maior:
        maior = peso
        print(f"maior: {maior}")
    if peso < menor:
        menor = peso
        print(f"menor: {menor}")

print(f"""
O maior foi: {maior}
O menor foi: {menor}
""")
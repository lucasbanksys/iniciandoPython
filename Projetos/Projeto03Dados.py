from time import sleep
from random import randint

# declaracao de variaveis zeradas ou vazias

vitoriasJog1 = 0
vitoriasJog2 = 0
vitoriasJog3 = 0
vitoriasJog4 = 0
cont = 0
grandeVencedor = ""


# quantidade de rodadas que o programa vai executar

qtdeRodadas = int(input("Quantas rodadas você deseja jogar? "))

# impede que o usuario digite 0 ou um valor negativo

while qtdeRodadas <= 0:
    print("Opção inválida. Repita: ")
    qtdeRodadas = int(input("Quantas rodadas você deseja jogar? "))

 # enquanto a variavel cont for menor a variavel qtdeRodadas: vai executar o codigo abaixo

while cont < qtdeRodadas and qtdeRodadas != 0:         

# valores aleatorios para cada jogador de 1 a 6 (faces do dado)

    jogadores = {
        "jogador1" : randint(1,6),
        "jogador2" : randint(1,6),
        "jogador3" : randint(1,6),
        "jogador4" : randint(1,6),
    }

# verifica quem foi o vencedor de cada rodada entre os 4 jogadores

    if jogadores.get("jogador1") > jogadores.get("jogador2") and jogadores.get("jogador1") > jogadores.get("jogador3") and jogadores.get("jogador1") > jogadores.get("jogador4"):
        vitoriasJog1 += 1
    elif jogadores.get("jogador2") > jogadores.get("jogador1") and jogadores.get("jogador2") > jogadores.get("jogador3") and jogadores.get("jogador2") > jogadores.get("jogador4"):
        vitoriasJog2 += 1
    elif jogadores.get("jogador3") > jogadores.get("jogador1") and jogadores.get("jogador3") > jogadores.get("jogador2") and jogadores.get("jogador3") > jogadores.get("jogador4"):
        vitoriasJog3 += 1
    elif jogadores.get("jogador4") > jogadores.get("jogador1") and jogadores.get("jogador4") > jogadores.get("jogador2") and jogadores.get("jogador4") > jogadores.get("jogador3"):
        vitoriasJog4 += 1

# imprime o jogador e o dado que ele tirou em cada rodada (com pausa de 0.2s)

    for k, v in jogadores.items():
        print(f"O jogador {k} tirou {v} no dado.")
        sleep(0.2)
        
# deixa o dicionario em ordem reversa (maior para menor) utilizando o valor da chave como referencia

    ranking = sorted(jogadores.items(), key=lambda v: v[1], reverse=True)

# exibicao do nome ranking

    print("\n    RANKING: ")
    print("-="*20)               # imprimiu os simbolos -= vinte vezes 


# exibicao do ranking do primeiro ao quarto lugar (com pausa de 0.3s)
# o sorted transformou o dicionario jogadores em uma lista

    for i, v in enumerate(ranking):
        print(f"{i+1} lugar: {v[0]} com numero {v[1]} no dado.")
        sleep(0.3)

    print() # pula 1 linha 
    cont += 1        # adiciona 1 a variavel cont do while


# verificando quem foi o GRANDE VENCEDOR

if vitoriasJog1 > vitoriasJog2 and vitoriasJog1 > vitoriasJog3 and vitoriasJog1 > vitoriasJog4:
    grandeVencedor = "jogador1"
elif vitoriasJog2 > vitoriasJog1 and vitoriasJog2 > vitoriasJog3 and vitoriasJog2 > vitoriasJog4:
    grandeVencedor = "jogador2"
elif vitoriasJog3 > vitoriasJog1 and vitoriasJog3 > vitoriasJog2 and vitoriasJog3 > vitoriasJog4:
    grandeVencedor = "jogador3"
elif vitoriasJog4 > vitoriasJog1 and vitoriasJog4 > vitoriasJog2 and vitoriasJog4 > vitoriasJog3:
    grandeVencedor = "jogador4"
else:
    grandeVencedor = "Não houve um grande vencedor"

# exibicao de quantas vezes cada jogador ganhou e quem foi o GRANDE VENCEDOR

print(f"""

O jogador1 ganhou {vitoriasJog1} vez(es).
O jogador2 ganhou {vitoriasJog2} vez(es).
O jogador3 ganhou {vitoriasJog3} vez(es).
O jogador4 ganhou {vitoriasJog4} vez(es).

O GRANDE VENCEDOR FOI: {grandeVencedor}!!

""")
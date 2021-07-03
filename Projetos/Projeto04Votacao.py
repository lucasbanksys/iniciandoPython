# importação da biblioteca para trabalhar com datas
from datetime import datetime

# importação da bibliteca para poder limpar a tela do console antes de executar o programa
from os import system

# inicialização de variáveis
numeroDoVoto = [0,0,0,0,0]

# limpeza da tela do console
system('cls')

# função autoriza_voto: recebe o anoNascimento como argumento e verifica se pela idade (calculada na função) o voto é OPCIONAL, NEGADO ou OBRIGATORIO
def autoriza_voto(anoNascimento):
    anoAtual = datetime.now().year
    idade = anoAtual - anoNascimento
    if idade > 65 or 16 <= idade < 18:
        return "OPCIONAL"
    elif idade < 16:
        return "NEGADO"
    elif idade > 18:
        return "OBRIGATORIO"

# funçao votação(): recebe dois parâmetros 1) autorização que vem do retorno da função autoriza_voto() e 2) voto que é o input do usuário

# se o parametro autorização for NEGADO exibe "Você não poder votar!" e nenhum voto será contabilizado
def votacao(autorizacao, voto):
    if autorizacao == "NEGADO":
        print("Você não pode votar!")

# se o parametro autorizacao for OPCIONAL ou OBRIGATORIO e se o valor de voto estiver entre 1 e 5 adiciona 1 voto pra o candidato. Cada voto será armazenado em um valor da lista numeroDoVoto
    elif autorizacao == "OPCIONAL" or autorizacao == "OBRIGATORIO":
        if 0 < voto < 6:      
            if autorizacao != "NEGADO":
                numeroDoVoto[voto-1] += 1
                print(f"""
    O Candidato 01 teve: {numeroDoVoto[0]} voto(s).
    O Candidato 02 teve: {numeroDoVoto[1]} voto(s).
    O Candidato 03 teve: {numeroDoVoto[2]} voto(s).
    Votos nulos: {numeroDoVoto[3]} voto(s).
    Votos em branco: {numeroDoVoto[4]} voto(s).
                """)
        # se o voto estiver fora das opções (1, 2, 3, 4, 5), exibe
        else: 
            print("Você inseriu uma opção de voto inválida. Votação cancelada para esse eleitor.")


# codigo principal

while True:
    candidato = str(input(f"Nome do(a) o(a) eleitor(a): "))
    anoNascimento = int(input("Digite seu ano de nascimento: "))
    autorizacao = autoriza_voto(anoNascimento)
    voto = int(input("Voto [1-5]: "))
    # enquanto a funcao votacao() retornar "Você inseriu uma opção de voto inválida. Votação cancelada para esse eleitor." vai continuar pedindo o input do voto
    while votacao(autorizacao, voto) == "Você inseriu uma opção de voto inválida. Votação cancelada para esse eleitor.":
        voto = int(input("Voto [1-5]: "))
    
# variavel que informa se quer continuar adicionando eleitores
    continua = str(input("Digite N para parar ou qualquer outra tecla para continuar: ")).upper().strip()[0]
    if continua == "N":
        break

# verificação do vencedor da eleição
if numeroDoVoto[0] > numeroDoVoto[1] and numeroDoVoto[0] > numeroDoVoto[2] and numeroDoVoto[0] > numeroDoVoto[3] and numeroDoVoto[0] > numeroDoVoto[4]:
    vencedor = "Candidato 01"
elif numeroDoVoto[1] > numeroDoVoto[0] and numeroDoVoto[1] > numeroDoVoto[2] and numeroDoVoto[1] > numeroDoVoto[3] and numeroDoVoto[1] > numeroDoVoto[4]:
    vencedor = "Candidato 02"
elif numeroDoVoto[2] > numeroDoVoto[0] and numeroDoVoto[2] > numeroDoVoto[1] and numeroDoVoto[2] > numeroDoVoto[3] and numeroDoVoto[2] > numeroDoVoto[4]:
    vencedor = "Candidato 03"
else:
    vencedor = "Não houve vencedor"

print(f"\nO vencedor foi: {vencedor}!")
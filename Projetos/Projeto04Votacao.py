from datetime import datetime


candidatos = list()
listaCandidatosESeusVotos = dict()
listaVotos = list()
continua = "S"

def autoriza_voto(anoNascimento):
    anoAtual = datetime.now().year
    idade = anoAtual - anoNascimento
    if idade > 65 or 16 <= idade < 18:
        return "OPCIONAL"
    elif idade < 16:
        return "NEGADO"
    elif idade > 18:
        return "OBRIGATORIO"


def votacao(autorizacao, voto):

    for i in range(1):
        votosCandidato1 = 0
        votosCandidato2 = 0
        votosCandidato3 = 0
        votosNulos = 0
        VotosEmBranco = 0

    if autorizacao == "NEGADO":
        print("Você não pode votar!")

    elif autorizacao == "OPCIONAL" or autorizacao == "OBRIGATORIO":
        if 0 < voto < 6:
            

            if autorizacao != "NEGADO":
                if voto == 1:
                    votosCandidato1 += 1
                elif voto == 2:
                    votosCandidato2 += 1
                elif voto == 3:
                    votosCandidato3 += 1
                elif voto == 4:
                    votosNulos += 1
                elif voto == 5:
                    VotosEmBranco += 1
                
                print(f"""
O candidato 01 teve: {votosCandidato1} votos.
O candidato 02 teve: {votosCandidato2} votos.
O candidato 03 teve: {votosCandidato3} votos.
Votos nulos: {votosNulos} votos.
Votos em branco: {VotosEmBranco} votos.
""")
        else: 
            print("Você inseriu uma opção de voto inválida. Votação cancelada para esse eleitor.")


while continua != "N":
    candidato = str(input(f"Nome do(a) o(a) eleitor(a): "))
    anoNascimento = int(input("Digite seu ano de nascimento: "))
    autorizacao = autoriza_voto(anoNascimento)
    voto = int(input("Voto [1-5]: "))
    while votacao(autorizacao, voto) == "Você inseriu uma opção de voto inválida.":
        voto = int(input("Voto [1-5]: "))
    
    continua = str(input("Deseja adicionar outro eleitor? [S/N]: ")).upper().strip()[0]



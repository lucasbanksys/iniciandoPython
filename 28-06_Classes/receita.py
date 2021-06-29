from time import sleep

class Receita:
    def __init__(self, ovo, leite, farinha, manteiga):
        self.ovo = ovo
        self.leite = leite
        self.farinha = farinha
        self.manteiga = manteiga

    
    def misturar(self):
        if self.ovo == 5:
            return "Bolo sendo misturado..."
        else:
            return "Você precisa de dois ovos para misturar o bolo"

    def assar(self):
        print("Bolo sendo preparado....")
        sleep(2)
        print("O bolo foi preparado!!!")

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura


    def Envelhecer(self):
        
        self.idade += 1
        print(f"Você envelheceu um ano. Sua idade agora é {self.idade}.")
        if self.idade < 21:
            self.altura += 0.05

    def Engordar(self):
        pass

    def Emagrecer(self):
        pass

    def Crescer(self):
        pass

    def MostrarDados(self):
        return f'''
Nome = {self.nome}
Idade = {self.idade}
Peso = {self.peso}
Altura = {self.altura}
        '''

pessoa1 = Pessoa("Lucas", 15, 60.0, 1.50)

print(pessoa1.MostrarDados())

pessoa1.Envelhecer()

print(pessoa1.MostrarDados())
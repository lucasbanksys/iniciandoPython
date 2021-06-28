class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nomePessoa = nome
        self.idadePessoa = idade
        self.pesoPessoa = peso

    def comer(self,calorias):
        self.pesoPessoa = self.pesoPessoa + calorias

    def malhar(self, calorias):
        self.pesoPessoa -= calorias

    def mostrarDados(self):
        print(f"""
        Nome = {self.nomePessoa}
        Idade = {self.idadePessoa}
        Peso = {self.pesoPessoa}
        """)

pessoa1 = Pessoa("Lucas", 28, 57.0) # instanciando (criando) um objeto
pessoa2 = Pessoa("Maria", 29, 72.0)

pessoa1.mostrarDados()

pessoa1.comer(5)

pessoa1.mostrarDados()

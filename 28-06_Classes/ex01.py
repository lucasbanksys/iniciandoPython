class Conta:
    def __init__(self,titular, saldo):
        self.titularPessoa = titular
        self.saldoPessoa = saldo

    def Sacar(self, saque):
        if saque >= self.saldoPessoa:
            return "Saldo insuficiente para o valor de saque desejado."
        else:
            self.saldoPessoa -= saque
            return f"Você sacou {saque} reais."

    def Depositar():
        pass

    def mostrarDados(self):
        return f"""
        Titular = {self.titularPessoa}
        Saldo = {self.saldoPessoa}
        """

pessoa1 = Conta("Lucas", 2000)

print(pessoa1.mostrarDados())

print(pessoa1.Sacar(4000))

print(pessoa1.mostrarDados())

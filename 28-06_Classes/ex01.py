# SIMULAÇÃO CAIXA ELETRONICO - SAQUE/DEPÓSITO


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

    def Depositar(self, deposito):
        self.saldoPessoa += deposito
        return f"Você depositou {deposito} reais."
        

    def mostrarDados(self):
        return f"""
        Titular = {self.titularPessoa}
        Saldo = {self.saldoPessoa}
        """

pessoa1 = Conta("Lucas", 2000)

print(pessoa1.mostrarDados())

print(pessoa1.Sacar(400))

print(pessoa1.mostrarDados())

print(pessoa1.Depositar(300))

print(pessoa1.mostrarDados())

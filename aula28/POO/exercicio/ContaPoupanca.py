from Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, titular, senha, deposito):
        super().__init__(titular, 0, senha)
        self.saldo = deposito
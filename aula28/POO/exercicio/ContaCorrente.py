from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, titular, senha, limite):
        super().__init__(titular, 0, senha)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            return True
        return False

    def verifica_saldo(self):
        info = f"Seu saldo é de R${self.saldo:.2f}"
        if self.saldo < 0:
            info += f"Limite disponível: R${(self.saldo + self.limite):.2f}"
        else:
            info += f"Limite disponível: R${self.limite:.2f}"
        return info


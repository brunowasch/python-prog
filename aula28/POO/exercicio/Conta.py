import random

class Conta:
    def __init__(self, titular, saldo, senha):
        self.titular = titular
        self.saldo = saldo
        self.senha = senha
        self.identificador = self.gera_identificador()

    def gera_identificador(self):
        id = ""
        for _ in range(5):
            aleatorio = random.randint(0, 9)
            id += str(aleatorio)
        return id
    
    def depositar(self, valor):
        self.saldo += valor

    def valida_acesso(self, identificador, senha):
        return self.identificador == identificador and self.senha == senha
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo-=valor
            return True
        return False
    
    def verifica_saldo(self):
        return f"Seu saldo é de {self.saldo:.2f}"

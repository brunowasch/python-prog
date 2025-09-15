class Conta():
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    # Getter:
    @property
    def saldo(self):
        return self.__saldo
    
    # Setter:
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print('Não é possível alterar o saldo.')
        else:
            self.__saldo = valor

conta_um = Conta('Jonas', 100)
# O acesso ao getter e setter criados do jeito Pyhton se comportam com um acesso direto à variável
print(conta_um.saldo)
# Acesso ao setter
conta_um.saldo = 1000
#Acesso ao getter
print(conta_um.saldo)
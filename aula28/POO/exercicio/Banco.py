from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

class Banco:
    @staticmethod
    def le_string(mensagem: str) -> str:
        return input(mensagem + ": ")

    @staticmethod
    def le_float(mensagem: str) -> float:
        while True:
            try:
                return float(input(mensagem + ": "))
            except ValueError:
                print("Por favor, digite um número válido.")

    @staticmethod
    def acessa_cc(c1: ContaCorrente) -> ContaCorrente:
        print(f"Acessando a conta {c1.identificador}")
        print(f"Bem-vindo, {c1.titular}")
        while True:
            print("\nSelecione uma opção")
            print("d - realizar um depósito")
            print("s - realizar um saque")
            print("v - verificar o saldo")
            print("a - alterar a senha")
            print("e - sair")
            opc = Banco.le_string("").lower()
            match opc:
                case "d":
                    valor = Banco.le_float("Qual valor deseja depositar")
                    c1.depositar(valor)
                    print("Depósito realizado!")
                case "s":
                    valor = Banco.le_float("Qual o valor do saque")
                    if c1.sacar(valor):
                        print("Saque realizado")
                    else:
                        print("Saldo mais limite insuficientes")
                case "v":
                    print(c1.verifica_saldo())
                case "a":
                    nova = Banco.le_string("Qual a nova senha")
                    c1.senha = nova
                    print("Senha alterada com sucesso!")
                case "e":
                    break
                case _:
                    print("Opção inválida.")
        return c1

    @staticmethod
    def acessa_cp(c1: ContaPoupanca) -> ContaPoupanca:
        print(f"Acessando a conta {c1.identificador}")
        print(f"Bem-vindo, {c1.titular}")
        while True:
            print("\nSelecione uma opção")
            print("d - realizar um depósito")
            print("s - realizar um saque")
            print("v - verificar o saldo")
            print("a - alterar a senha")
            print("e - sair")
            opc = Banco.le_string("").lower()
            match opc:
                case "d":
                    valor = Banco.le_float("Qual valor deseja depositar")
                    c1.depositar(valor)
                    print("Depósito realizado!")
                case "s":
                    valor = Banco.le_float("Qual o valor do saque")
                    if c1.sacar(valor):
                        print("Saque realizado")
                    else:
                        print("Saldo insuficiente")
                case "v":
                    print(c1.verifica_saldo())
                case "a":
                    nova = Banco.le_string("Qual a nova senha")
                    c1.senha = nova
                    print("Senha alterada com sucesso!")
                case "e":
                    break
                case _:
                    print("Opção inválida.")
        return c1

    @staticmethod
    def cadastra_cc() -> ContaCorrente:
        titular = Banco.le_string("Qual o titular da conta")
        senha = Banco.le_string("Qual a senha")
        limite = Banco.le_float("Qual o limite inicial")
        c1 = ContaCorrente(titular, senha, limite)
        print(f"Conta cadastrada com o identificador {c1.identificador}")
        return c1

    @staticmethod
    def cadastra_cp() -> ContaPoupanca:
        titular = Banco.le_string("Qual o titular da conta")
        senha = Banco.le_string("Qual a senha")
        deposito = Banco.le_float("Qual valor depositar")
        c1 = ContaPoupanca(titular, senha, deposito)
        print(f"Conta cadastrada com o identificador {c1.identificador}")
        return c1


if __name__ == "__main__":
    lista_cc: list[ContaCorrente] = []
    lista_cp: list[ContaPoupanca] = []
    MAX = 20

    while True:
        print("\nSelecione uma opção")
        print("cc - cadastrar conta corrente")
        print("cp - cadastrar conta poupança")
        print("ac - acessar conta corrente")
        print("ap - acessar conta poupança")
        print("e  - sair")
        opc = Banco.le_string("").lower()

        match opc:
            case "cc":
                if len(lista_cc) >= MAX:
                    print("Limite de contas correntes atingido.")
                else:
                    lista_cc.append(Banco.cadastra_cc())

            case "cp":
                if len(lista_cp) >= MAX:
                    print("Limite de contas poupança atingido.")
                else:
                    lista_cp.append(Banco.cadastra_cp())

            case "ac":
                identificador = Banco.le_string("Qual o identificador")
                senha = Banco.le_string("Qual a senha")
                pos = next((i for i, conta in enumerate(lista_cc)
                            if conta.valida_acesso(identificador, senha)), -1)
                if pos >= 0:
                    lista_cc[pos] = Banco.acessa_cc(lista_cc[pos])
                else:
                    print("Conta inexistente ou senha incorreta!")

            case "ap":
                identificador = Banco.le_string("Qual o identificador")
                senha = Banco.le_string("Qual a senha")
                pos = next((i for i, conta in enumerate(lista_cp)
                            if conta.valida_acesso(identificador, senha)), -1)
                if pos >= 0:
                    lista_cp[pos] = Banco.acessa_cp(lista_cp[pos])
                else:
                    print("Conta inexistente ou senha incorreta!")

            case "e":
                print("Encerrando...")
                break

            case _:
                print("Opção inválida!")
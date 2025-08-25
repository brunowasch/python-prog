n1 = int(input("Digite um número:\n"))
n2 = int(input("Digite o segundo número:\n"))
op = input("Digite a operação (+, -, /, *, **)")

match op:
    case '+':
        print(n1+n2)
    case '-':
        print(n1-n2)
    case '/':
        print(n1/n2)
    case '*':
        print(n1*n2)
    case '**':
        print(n1**n2)
    case _:
        print("Números inválidos!")
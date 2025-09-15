def divide(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError('Não podemos dividir por zero.')
    return n1/n2

print(divide(5,0)) # print(divide(n1 = 5, n2 = 0))
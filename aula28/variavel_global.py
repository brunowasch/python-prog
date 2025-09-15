x = 10 # Variável global

def soma(valor):
    global x # Passa o valor de x para a função
    x += valor + 10 # Não funciona sem o global
    print(x)
soma(5)
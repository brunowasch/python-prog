# Tratamento de exceções

try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    resp = n1/n2
except ZeroDivisionError:
    print("Ocorreu um erro ao tentar dividir por zero.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
else: 
    print("Só serei executado se não houver problemas.")
finally:
    print("Sempre serei executado.")
print("Restante do código...")
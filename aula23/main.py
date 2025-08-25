#Código em Python
import math
nota_um = float(input('Digite a primeira nota: '))
nota_dois = float(input('Digite a segunda nota: '))
media = (nota_um+nota_dois)/2

print(f"\nA média é {media:.2f}")
print("A média é", media,"\n")
print(f"Nota 1: {nota_um:.2f} \nNota 2: {nota_dois:.2f}\n")
if media >= 6:
    print(f"Aprovado. Média final: {media:.2f}")
elif media <= 5:
    print(f"Reprovado. Média final: {media:.2f}")
else:
    print("Valor inválido!")

print(math.sqrt(144)) 

a = 10
b=15
print(a<10 or b>10)

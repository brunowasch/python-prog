from collections import Counter

palavra = 'teste'
letras = Counter(palavra)
letras.update('testando')
print(letras)

c1 = Counter(a = 3, b = 1)
c2 = Counter(a = 1, b = 2, c = 3)
print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c1 & c2)
print(c1 | c2)
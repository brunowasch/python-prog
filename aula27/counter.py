from collections import Counter
lista = [1,1,2,3,4,4,1,5,5,6]
contador = Counter(lista)
print(contador)
print(contador.get(1, 'Chave não encontrada'))

conjunto = {1,2,3,4,5}
print(conjunto)
conjunto = set([1,2,3,4,5,5,5,5,5,5])
print(conjunto)

c1 = conjunto = {1,2,3,4}
c2 = conjunto = {3,4,5,6}
#União de dois conjuntos
print(c1 | c2)
#Interseção de dois conjuntos
print(c1 & c2)

c1 = conjunto = {1,2,3,4}
c2 = conjunto = {3,4,5,6}

#Diferença de dois conjuntos
c3 = c1 - c2
print(c3)

#Diferença de dois conjuntos
c4 = c2 - c1
print(c4)
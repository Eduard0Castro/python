lista = [item*2 for item in range(5)]
print(lista)

pares = [num for num in range(21) if num%2==0]
print(pares)

#Coloca 3 vezes i e contagem de j para todo i ímpar:
hugo = [(i,j) for i in range (10)  for j in range (3) if i%2!=0]
#ou [(i,j) for i in range (10) if i%2!=0 for j in range (3)]
print(hugo)

lucio = [kiko if kiko %2 == 0 else kiko*2 for kiko in range(10)]
print(lucio)

inside = [[i+1 for i in range (4)] for v in range(3)]

print(inside)
from random import randint

vector = [randint(0, 100) for x in range(20)]
pares = [x for x in vector if x%2 == 0]
impar = [x for x in vector if x%2 != 0]

print(vector)
print(pares)
print(impar)
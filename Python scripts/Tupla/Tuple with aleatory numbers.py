from random import randint

tupla = (randint(0, 10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
menor = tupla[0]
maior = tupla[0]


for i in range (0, len(tupla)):

    if (tupla[i] < menor):
        menor = tupla[i]

    if (tupla[i] > maior):
        maior = tupla[i]


print(tupla)
print(maior)
print(menor)
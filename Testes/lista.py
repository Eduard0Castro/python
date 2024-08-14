from statistics import mean
from random import randint

lista = [randint(0, 10) for i in range(10)]

print(lista)
lista.clear()
print(lista)
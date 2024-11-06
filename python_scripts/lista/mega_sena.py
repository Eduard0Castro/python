from random import randint
from time import sleep

n = int(input("Digite quantos jogos serão gerados: "))

s = 0
inter = []
hugo = []

primeiro = True
for i in range (0, n):
    for j in range (0,6):
       
        while s in inter or primeiro:
            s = randint(1, 60)
            primeiro = False
        inter.append(s)
   
    inter.sort()
    hugo.append(inter[:])
    inter.clear()

print("\nJogos sorteados:")
for pos, c in enumerate(hugo):
    print(f"Jogo {pos+1}: {c}")
    sleep(1)
    





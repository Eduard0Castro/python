from random import randint

num = randint(0,10)
usu = 11
while usu != num:
    usu = int(input('Digite um número inteiro de 0 a 10: '))

print('\033[32mVocê acertou!!!\033[m')
print(num)

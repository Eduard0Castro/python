from random import randint

numero = randint(0,5)
print(numero)
n = int(input('Digite um numero inteiro entre 0 e 5: '))

while numero != n:
    print('Não é esse o número, tente novamente: ')
    n = int(input('Digite um numero inteiro entre 0 e 5: '))

if numero == n:
    print('Parabéns, você acertou o número!')


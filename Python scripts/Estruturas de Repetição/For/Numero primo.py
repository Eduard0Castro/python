
n = int(input('Digite um numero inteiro para saber se é um número primo: '))
count = 0
mult = 0
for i in range (2, n + 1):
    if n%i == 0:
        print(f'É múltiplo de {i}')
        mult += 1

if mult == 1:
    print('\033[1;32mÉ um número primo!!!\033[m') 

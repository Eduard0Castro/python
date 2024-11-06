n = 0

while 1:
    n = int(input('Digite um valor para ver sua tabuada: '))

    if(n < 0):
        break

    for i in range(1, 11):
        print(f'{i} X {n} = {n*i}')

print("\033[31mAcabou\033[m")
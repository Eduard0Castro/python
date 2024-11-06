ni = int(input('Digite um número inteiro: '))

s = ni + 1
a = ni - 1

#print('\nAntecessor: {}, Sucessor: {}\n' .format(a,s))

for j in range(1, ni + 1):
    j = ni - j 
    e = ni -1 -j #abs(j - (ni-1)) # j + 1 - ni => ni -j -1
    print('{}' .format(e), end = ' ')
    if e == ni-1:
        print('>>> ', end = '')
for h in range (0, ni+1):
     h = h + ni
     print('{}' .format(h), end = ' ')
     if h == ni:
         print('>>> ', end = '')
     if h == 2*ni:
        print('\n')







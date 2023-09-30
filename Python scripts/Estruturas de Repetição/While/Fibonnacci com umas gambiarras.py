n = int(input('Quantas numeros da sequência de Fibonnacci você deseja ver? '))
cont = 0
t1 = 0
t2 = 1

print(t1, t2, end =' ')
while n != 0:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print(t3, end = ' ')
    if cont == n:
        n = int(input('\nQuantos termos mais você quer ver? '))
        cont = 0
       
        

print('\n')



    
    
    
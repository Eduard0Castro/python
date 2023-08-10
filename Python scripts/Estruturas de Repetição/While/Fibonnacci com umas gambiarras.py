n = int(input('Quantas numeros da sequência de Fibonnacci você deseja ver? '))
cont = 0
t1 = 0
t2 = 1
rep = n
rep_2 = rep
print(t1, t2, end =' ')
while rep_2 != 0:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print(t3, end = ' ')
    if cont == rep -2:
        rep = int(input('\nQuantos termos mais você quer ver? '))
        cont = 0
        rep_2 = rep
        rep = rep +2 

print('\n')



    
    
    
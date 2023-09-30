from math import ceil
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

menu = int
while menu != 5:
    menu = int(input('\nDigite qual operação você gostaria de realizar com esses dois números: \n[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão\n[5]Sair do programa\n-- '))
    if menu == 1:
        soma = n1 + n2
        print('\033[32m\nResultado : {}\033[m'. format(soma))
        result = soma
    if menu == 2:
        sub = n1 - n2
        print('\033[32m\nResultado : {}\033[m'. format(sub))
        result = sub
    if menu == 3:
        mult = n1*n2
        print('\033[32m\nResultado : {}\033[m'. format(mult))
        result = mult
    if menu == 4:
        div = n1/n2
        print('\033[32m\nResultado : {:.2f}\033[m'. format(div))
        result = div

result = ceil(result)
print ('Resultado da última operação: {}' .format(result))


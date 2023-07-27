ano = int(input('Digite o ano para saber se é bissexto: '))

if ano%4 == 0:
    print('{} é um ano bissexto' .format(ano))

else:
    print('\033[31m{} não é um ano bissexto!' .format(ano))




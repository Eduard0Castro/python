ano = int(input('Digite o ano para saber se é bissexto: '))

if ano%4 == 0:
    print(f'\033[32m{ano} é um ano bissexto')

else:
    print(f'\033[31m{ano} não é um ano bissexto!\033[m' )




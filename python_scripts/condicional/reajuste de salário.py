sal = float(input('Digite o valor do seu salário: R$'))

if sal > 1250:
    print('Seu novo salário é de R${:.2f}' .format(sal*1.1))

else:
    print('Seu novo salário é de R${:.2f}' .format(sal*1.5))

    
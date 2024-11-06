n = []
i = []
s = []
heil = 0
cont = 0
maior = 0
for p in range(0,4):
    print('\n-', f'{p+1}ª Pessoa: -\n', )
    nome = str(input('Digite seu nome: ')).capitalize().strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo[M/F]: ')).capitalize().strip()
  
    heil += idade
    if sexo == 'F' and idade < 20:
        cont +=1

    if sexo == 'M':
        if idade > maior:
            maior = idade
            velho = nome
print('\nO homem mais velho: {}'.format(velho))
print(f'\nA quantidade de mulheres que têm menos de 20 anos é {cont}')
media = heil/4
print('\nA média das idades das pessoas é', media)



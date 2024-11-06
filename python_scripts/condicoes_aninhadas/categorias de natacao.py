from datetime import datetime

ano_atual = datetime.today().year
nasc = str(input('Digite a sua data de nascimento: '))
div = nasc.split('/')
ano_nasc = int(div[2])
idade = ano_atual - ano_nasc
print(idade)

if idade < 9:
    print('Categoria mirim!')
elif 9 < idade < 14:
    print('Categoria infantil!')
elif 14 <= idade < 19:
    print('Categoria junior!')
elif 19 <= idade < 20:
    print('Categoria senior!')
else:
    print('\033[1;32mCategoria Master!\033[m')


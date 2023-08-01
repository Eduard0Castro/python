from datetime import datetime
ano = str(input('Digite a sua data de nascimento com o dia o mes e o ano separados por espaço: '))

ano = ano.split()
print(ano)
ano_i = int(ano[2])
data_atual = datetime.today()
print(data_atual.year)
idade = data_atual.year - ano_i
print(idade)

if idade > 16:
    print(f'\n\033[31mJá passou do tempo de alistamento por {(idade - 16 )} anos!\033[m')

elif idade == 16:
    print('\n\033[34mJá é hora de se alistar, meu valente soldado!\033[m')

else:
    print(f'\n\033[32mAinda falta {16 - idade} anos para você se alistar!\033[m')
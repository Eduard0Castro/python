from datetime import datetime

data = datetime.today()
year = data.year
cont = 0
for i in range (0,7):
    ano = int(input('Digite o seu ano de nascimento: '))
    if (year - ano) < 18:
        cont += 1

print(f'{cont} pessoas ainda não atingiram a maioridade!')



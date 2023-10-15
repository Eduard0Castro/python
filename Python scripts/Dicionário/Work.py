from datetime import datetime
data = datetime.today()
year = data.year
trabaia = {}

trabaia['Nome'] = str(input("Digite o seu nome: "))
ano = int(input("Digite o seu ano de nascimento: "))
trabaia['Idade'] = year - ano
trabaia['Carteira de Trabalho'] = int(input("Tem carteira de trabalho?(0-> Não tem!) "))

if trabaia["Carteira de Trabalho"] != 0:
    trabaia['Ano de contratação'] = int(input("Digite o seu ano de contratação: "))
    trabaia['Salário'] = float(input("Digite o seu salário: "))
    trabaia['Aposentá'] = trabaia['Ano de contratação'] + 35 - ano

print('')
print("=-"*30)

for pos, c in trabaia.items():
    print(f"{pos} tem o valor {c}")

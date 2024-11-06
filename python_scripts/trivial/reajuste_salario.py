
salario = float(input('Informe seu salario: '))

if salario < 500:
    ajuste1 = (salario*1.15)
    print('Ajuste de 15%:', ajuste1)
    
if 500 < salario < 1000:
    print('Ajuste de 10%:', salario*1.10)

if salario > 1000:
    print('Ajuste de 5%:', salario*1.05)

else :
    print('Salario de idiota o seu')


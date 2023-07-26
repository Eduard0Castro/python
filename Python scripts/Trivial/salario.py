import time 

time.sleep(0)

salario = (input('Digite o seu salário: '))
valor = salario*1.15
print(salario.isnumeric())
print('O seu novo salario sera: {:.2f}' .format(valor))

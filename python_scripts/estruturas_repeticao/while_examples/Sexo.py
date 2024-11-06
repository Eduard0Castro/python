sexo = str(input('Digite seu sexo[M/F]: ')).upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Não é um sexo válido(???), digite novamente: ')).upper()

print('Okay, seu sexo é ', end = '')

print('Masculino' if sexo == 'M' else 'Feminino')


nome = str(input('Digite seu nome completo: ')).strip()

div = nome.split()

print('Seu primero nome é {} \nE seu último nome é {}' .format(div[0], div[len(div)-1]))


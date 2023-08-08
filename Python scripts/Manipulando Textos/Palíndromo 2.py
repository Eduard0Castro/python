frase = str(input('Digite uma frase para verificar se é um palíndromo: ')).strip().lower()

div = frase.split()
junto = ''.join(div)
inver = ''

for i in range (len(junto) - 1, -1, -1):
    inver += junto[i]
    
if inver == junto:
    print('\033[32mÉ um palíndromo!!!\033[m')
else:
    print('\033[31mNão é um palíndromo..\033[m')


from unidecode import unidecode

n = int(input('Digite um numero inteiro: '))
base = unidecode(str(input('\nPara qual base numerica você quer converter esse número?\nSuas opções são:\n\033[32mBinário\033[m\n\033[34mOctal\033[36m\nHexadecimal\033[m\n--')).lower())
print(base)
if base == 'hexadecimal':
    print(f'Hexadecimal: {hex(n)}')

elif base == 'octal':
    print(f'Octal: {oct(n)}')
elif base == 'binario':
    print(f'Binário: {bin(n)}')
else:
    print('\033[31mReveja a digitação!\033[m')





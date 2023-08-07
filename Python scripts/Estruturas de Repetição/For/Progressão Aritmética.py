termo = float(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite uma razão inteira para a progressão aritmética: '))

for i in range(0,10):
    print(termo, end = ' ')
    termo = termo + razao
    
print('\n')

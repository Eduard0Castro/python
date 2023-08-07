peso  = 0
maior = 0
for i in range (0,5):
    
    peso = float(input('Digite o peso da pessoa {}: ' .format(i+1)))
    if peso > maior:
        maior = peso

print('O maior peso é {}' .format(maior))



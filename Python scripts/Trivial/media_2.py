import time 

soma = 0
notas = int(input('Quantas notas serão aplicadas? '))
nota = 0
for i in range (1, notas + 1):
    nota = float(input('Digite a nota {}: ' .format(i)))
    soma += nota

media = (soma) / notas
print('A media das notas é: {}' .format(media))


import random

q = int(input(('Quantos alunos participarão do sorteio? ')))
soma = []
for i in range (1, q+1):
    n = str(input('Digite o nome do aluno {}: ' .format(i)))
    soma += [n]
    

sorteado = random.choice(soma)

print('O escolhido foi: {}' .format(sorteado))
print('Mas poderia ter sido o: {}' .format(soma[3]))



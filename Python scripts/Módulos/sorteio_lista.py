from random import shuffle

q = int(input('Quantos alunos estarão presentes na lista? '))
soma = []

for i in range (1, q+1):
    n = str(input('Digite o nome do aluno {}: ' .format(i)))
    soma += [n]

shuffle(soma)

print('A ordem escolhida foi: {}' .format(soma))




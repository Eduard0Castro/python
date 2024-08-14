
alunos = [[str(input(f"Digite o nome do aluno {x+1}: ")), 
  int(input(f"Numero de matriculo do aluno {x+1}: ")), 
  float(input(f"Nota do aluno {x+1}: "))] for x in range(5)]

reprovados = list()
aprovados = list()

for aluno in alunos:
    reprovados.append(aluno) if aluno[2] < 6.0 else aprovados.append(aluno)
    
print("\nAprovados: ")

for aprovado in aprovados:
    for info in aprovado:
        print(info, end=", ")
    print()

print("\nReprovados: ")

for reprovado in reprovados:
    for info in reprovado:
        print(info, end=", ")



student = {'nome': '', 'media': '', 'situation': ''}

student['nome'] = str(input("Digite o nome do aluno: "))
student['media'] = float(input("Digite a media do aluno: "))

if student['media'] >= 7.0:
    student['situation'] = 'Aprovado'

else:
    student['situation'] = 'Reprovado'

print(f"Nome: {student['nome']}")
print(f"Média: {student['media']}")
print(f"Situação: {student['situation']}")


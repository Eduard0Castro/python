nome = str(input('Digite o nominho da criança: '))

print(nome.upper())
print(nome.lower())
print(len(nome)- nome.count(' '))
for i in nome:
    print(i, "--", end = '')

print("\n")
print(nome.split()[1])
print(len(nome.split()[0]))
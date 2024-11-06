people = {}
person = []
soma = 0
veios = []
nome = []

while True:

    people['Nome'] = str(input("Digite o nome do ser humano: "))
    people['Sexo'] = ''
    while people['Sexo'] != 'M' and people['Sexo'] != 'F':
        people['Sexo'] = str(input("Digite o sexo do ser humano: ")).upper()
    people['Idade'] = int(input("Digite a idade do ser humano: "))
    soma += people['Idade']
    person.append(people.copy())
    if people['Sexo'] == 'F':

        nome.append(people['Nome'])
    
    c = ""
    while c != 'N' and c != 'S':
        c = str(input("Quer continuar?[S/N]: ")).upper()

    if c == 'N':
        break

media = soma/len(person)

for c in person:
    if c['Idade'] > media:
        veios.append(c)


print("")
print(f"Foram cadastradas {len(person)} pessoas!")
print(f"Média: {media:.2f}")
print(f"Mulheres: {nome}")
print(f"Pessoas com idade acima da média: {veios}")
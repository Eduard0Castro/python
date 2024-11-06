hugo = list()
nomep = list()
nomel = list()
helton = list()
cont = 0

while True:
    hugo.append(str(input("Digite um nome: ")))
    hugo.append(int(input("Digite o peso: ")))
    helton.append(hugo[:])

    cont += 1
    if cont == 1:
        menor = maior = hugo[1]

    elif hugo[1] < menor:
        menor = hugo[1]

    elif hugo[1] > maior:
        maior = hugo[1]

    hugo.clear()
    p = ""
    while p != "N" and p != "S":
        p = str(input("Quer continuar? [S/N]: ")).upper()

    if p == "N":
        break

print(f"\nForam cadastradas {cont} pessoas!")


for j in helton:
    if menor in j:
        nomel.append(j[0])
    if maior in j:
        nomep.append(j[0])

print(f"Pessoas mais pesadas com o peso de {maior}: {nomep}")
print(f"Pessoas mais leves com o peso de {menor}: {nomel}")

soma = 0
for n in range (0,6):
    nu = int(input(f'Digite o {n +1}° número: '))
    if nu%2 == 0:
        soma += nu

print(f'A soma é {soma}')

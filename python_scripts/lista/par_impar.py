hugo = [[], []]

for i in range (0, 7):
    n = int(input("Digite o valor {}: " .format(i+1)))
    if n%2 == 0:
        hugo[0].append(n)
    else:
        hugo[1].append(n)

hugo[0].sort()
hugo[1].sort()
print("Os números pares são:" , hugo[0])
print("Os números ímpares são:", hugo[1])


n = 0
cont = 0
for i in range(0, 500, 3):
    if i%2 !=0:
        cont = cont +1
        n += i
print(f'\n\033[1;32mA soma dos {cont} numeros divisiveis por 3 é {n}\033[m')
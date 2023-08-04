seg_1 = str(input('Digite o comprimento de segmentos de reta separados por vírgula: ')).split(',')
seg = [int(seg_1[0]), int(seg_1[1]), int(seg_1[2]) ]
print(seg)
if ((seg[0] + seg[1]) > seg[2]) and ((seg [0] + seg[2]) > seg[1]) and ((seg[2] + seg[1]) > seg[0]):
    if seg[0] == seg[1] == seg[2]:
        print('\033[34mO triângulo é equilátero!\033[m')
    elif seg[0] == seg[1] or seg[1] == seg[2] or seg[0] == seg[2]:
        print('\033[35mO triângulo é isósceles!\033[m')
    else:
        print('\033[32mO triângulo é escaleno!\033[m')

else:
    print('\033[31mOs segmentos de reta não podem formar um triângulo!\033[m')
    
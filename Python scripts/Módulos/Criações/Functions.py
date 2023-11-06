def factorial (num):
    fat = 1
    for i in range (num, 0, -1):
        fat *= i

    return fat

def vector(lista):
    
    for i in lista:
        print(i, end=' ')

    print("")
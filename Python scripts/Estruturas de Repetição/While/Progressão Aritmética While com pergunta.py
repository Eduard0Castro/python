
termo = int(input('Digite o primero termo da pa: '))
razao = int(input('Digte a razao da pa: '))

rep = 10
cont = 0
ohmy = 1
while ohmy!=0:
    cont +=1
    print(termo, end=' ')
    termo = termo + razao
    if cont == rep:
        ohmy = int(input('\nQuer mostrar mais quantos números?? '))
        rep = ohmy
        cont = 0


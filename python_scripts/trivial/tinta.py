import time 

altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))

area = altura*largura

tinta = area/2

print('A area é {:.2f}m² e a quantidade de tinta necessária é {:.2f}L' .format(area, tinta))


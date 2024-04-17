from math import sqrt

#Usada para passar uma função simples como parâmetro para outra função
#Utilização:
square = lambda x: sqrt(x)

#Sem parâmetro de função:
nothing = lambda :2**3

hugo = [(1,6), (0, -2), (3,4), (4,8)]
print(square(16))
print(nothing())

hugo.sort(key=lambda x:x[0])

print(hugo)

precos = [10,40,20,30]

impostos = list(map(lambda x:x*0.3, precos))
print(impostos)

add = lambda x, y: x+y

print(add(3,5))
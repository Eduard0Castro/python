"""


Sets não seguem uma ordem, eles podem aparecer aleatoriamente nos prints
Não aceitam elementos duplicados
Geralmente, se utiliza sets para eliminar elementos duplicados. Unico porem é que essa lista retorna fora 
da ordem


Functions e symbols:

union: |
intersection: &
difference: -
symmetric_difference ^

"""

calderano = set()

calderano.add(4)
calderano.add("Lugar")
print(calderano)

calderano.update("Iteravel")
print(calderano)

add_tuple = (9,8,7,4,3)
calderano.update(add_tuple)
calderano.add(add_tuple)
print(calderano)

#Não adiciona valores repetidos!
for i in range (10):
    calderano.add("I")

duplicados = [1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3]
sem_duplicados = list(set(duplicados))
print(sem_duplicados)

mais_set = {"kiko", "abelhudo", 7}
print(calderano|mais_set)

inter = {"kiko", "chaves", "moregard"}
print(mais_set ^ inter)



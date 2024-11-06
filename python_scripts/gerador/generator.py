from time import sleep

hugo = list()
kaique = list()

def normal():
    for i in range(100):
        hugo.append(i)
        sleep(0.1)


for c in hugo: print(c)

# Dados são gerados conforme são requisitados:

def gerar():
    for c in range(100):
        yield c
        sleep(0.01)

for element in gerar():
    print(element)

#Ou:

generator = (x for x in range(100))
print("\nGerador: \n")
for c in generator:
    print(c)

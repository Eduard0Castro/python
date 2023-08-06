n = []
i = []
s = []
heil = 0
velho = str
cont = 0
for p in range(0,4):
    nome = str(input('Digite seu nome: ')).capitalize().strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: ')).capitalize().strip()
    n.append(nome)
    i.append(idade)
    s.append(sexo)
    heil += idade
    if sexo == 'Fem' and idade < 20:
        cont +=1

print(cont)
media = heil/4
print(media)
print('\n',i)
print('\n',s)


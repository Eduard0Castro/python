palavra = str
frase = str(input('Digite uma frase para verificar se é um palíndromo: ')).strip().lower()
div = frase.split()
sem_espaco = []

count = 0 
inicio = 0
count_2 = 0

for palavra in div:
    if palavra != ' ':
        print(palavra)
        sem_espaco += palavra
        print(sem_espaco)
        count +=1
tam = len(sem_espaco)
tam_2 = tam

junta = '-'.join(sem_espaco)
print(junta.upper())
for i in range(0, tam):
    if sem_espaco[tam-1] == sem_espaco[inicio]:
        count_2 +=1
    tam -= 1
    inicio +=1
print(tam_2)
print(count_2)
if count_2 == tam_2:
    print('\033[32mÉ um palindromo!\033[m')
else:
    print('Não é um palíndromo!')


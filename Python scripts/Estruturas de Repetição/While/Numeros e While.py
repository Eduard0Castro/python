count = 0
media = 0
res = str
heil = 0
maior = 0
menor = 0

while res != 'N':
    
    n = float(input('Digite um numero: '))
    count +=1
    heil += n
    
    #para o primeiro valor digitado, menor e maior recebem n
    if count == 1:
        menor = n = maior

    if maior < n:
        maior = n

    if menor > n :
        menor = n 

    if count%5 == 0:
        res = str(input('Deseja continuar [S/N]: \n')).upper()
    
media = heil/count
print(f'O maior numero digitado foi {maior}\nO menor foi {menor}\nQuantidade de numero digitados: {count}\nMédia: {media}')
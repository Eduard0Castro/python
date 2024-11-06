tupla = ('zero', 'um', 'dois', 'três', 'quatro', 
         'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 
         'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = -1

while True:
    while num < 0 or num > 20:
        num = int(input("Digite um número entre 0 e 20: "))

        if num == 666:
            break

    if num == 666:
        break
    print(f"O número digitado foi {tupla[num]}")

    num = -1


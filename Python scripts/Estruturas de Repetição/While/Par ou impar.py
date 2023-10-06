from random import randint


cont = 0

while True:
    n = randint(0,10)
    esc = str(input("Par ou ímpar(P/I): ")).upper()

    if (esc != "P" and esc!="I"):
        print("Digitou errado idiota\n")
        break
   
    num = int(input("Escolha um número para jogar par ou ímpar: "))
    soma = n + num


    print ("Computador escolheu {} e você {}. Soma: {}" .format(n, num, soma))
    if esc == "P":
        if soma%2 == 0:
            print("Você venceu!\n")
            cont += 1
        else:
            print("Você perdeu!")
            break

    elif esc == "I":
        if soma%2 == 0:
            print("Você perdeu!\n")
            break
        else:
            print("Você ganhou!\n")
            cont += 1

    

print("Acabou!!!\nVocê venceu {} vezes" .format(cont))



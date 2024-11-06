def ReadInt(msg):

    while True:
        num = str(input(msg))
        if num.isnumeric():
            return num
            
        else:
            print("\033[31mErro, digite um número válido: \033[m")
            

num = ReadInt("Digita: ")
print("Você digitou o número: {}" .format(num))


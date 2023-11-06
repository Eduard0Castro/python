def readMoney(msg):

    while True:
        num = str(input(msg))
        if num.isdecimal() is not True:
            print("\033[31mERRO, DIGITA DE NOVO AÍ\033[31m")

        else:
            return num

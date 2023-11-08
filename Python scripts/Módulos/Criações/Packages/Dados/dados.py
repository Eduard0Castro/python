def readMoney(msg):

    while True:
        
        num = str(input(msg)).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print("\033[31mERRO, DIGITA DE NOVO AÍ\033[m")

        else:
            return float(num)

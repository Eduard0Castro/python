def voto(ano):
    from datetime import date
    data = date.today()

    if data.year - ano >= 18 and data.year - ano <= 70:
        return "\033[32mOBRIGATÓRIO\033[m"
    elif data.year - ano < 18 and data.year - ano >= 16 or data.year - ano > 70:
        return "\033[34mOPCIONAL\033[m"
    else:
        return "\033[31mNEGADO\033[m"




ano = int(input("Digite o seu ano de nascimento: "))

print(voto(ano))
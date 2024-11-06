def aumentar(value, porcentagem, formata = False):
    aumentado = value*(1 + porcentagem/100)
    if formata == True:
        return moeda(aumentado)
    return aumentado

def diminuir(value, porcentagem, formata = False):
    diminuido = value*(1 - porcentagem/100)
    if formata == True:
        return moeda(diminuido)
    return diminuido

def metade (value, formata = False):
    metade = value/2
    if formata == True:
        return moeda(metade)
    return metade

def dobro (value, formata = False):
    dobro = value*2
    if formata == True:
        dobro = moeda(dobro)
    return dobro

def moeda(value):
    return f"R${value}"

def all(value, aum, dim):
    print("-"*20)
    print(f"RESUMO DO VALOR:" .center(20))
    print("-"*20)

    print(f"Preço: \t\t{moeda(value)}")
    print(f"Dobro: \t\t{dobro(value, True)}")
    print(f"Metade: \t{metade(value, True)}")
    print(f"Aumento: \t{aumentar(value, aum, True)}")
    print(f"Diminui: \t{diminuir(value, dim, True)}")
    print("")
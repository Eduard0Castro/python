tupla = ("Padaria", "Almoxarifado", "Office", "Michael", 
         "Katharina", "Kiko", "Otorrinolaringologista", "Hurricane")

vogais = ("a", "e", "i", "o", "u")

for c in range(0, len(tupla)):
    print(f"As vogais em {tupla[c]} são: ", end ='') 
    for d in range (0, len(vogais)):
        if vogais[d] in tupla[c].lower():
            print(f"{vogais[d]}", end = ' ')

    print('')

print('')
for c in range(0, len(tupla)):
    print(f"As vogais em {tupla[c].upper()} são: ", end ='') 
    for g in range (0, len(tupla[c])):
        if tupla[c][g].lower() in vogais:
            if g < len(tupla[c]) - 1:
                print(f"{tupla[c][g].lower()}", end = ', ')
            else:
                print(f"{tupla[c][g]}")
        elif g == len(tupla[c]) - 1: #Para resolver o problema do Michael
            print('')
    
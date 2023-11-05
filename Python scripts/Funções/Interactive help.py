
while True:
    esc = str(input('Função ou biblioteca: '))
    if (esc.upper() == "FIM"):
        break
    help(esc)


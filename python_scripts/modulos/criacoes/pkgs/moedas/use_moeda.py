from python_scripts.modulos.criacoes.pkgs.moedas.moeda import all

while True:
    num = float(input("Digite o valor: "))

    if num == -1:
        break

    # print(f"Dimuído em 13%: {diminuir(num, 13, True)}")
    # print(f"Aumentado em 10%: {aumentar(num, 10, True)}")
    # print(f"Metade: {metade(num, True)}")
    # print(f"Dobro: {dobro(num, True)}")
    # print("")
    all(num, 80, 35)



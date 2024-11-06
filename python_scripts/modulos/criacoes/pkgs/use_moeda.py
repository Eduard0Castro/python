from python_scripts.modulos.criacoes.pkgs.moedas.moeda import all
from dados.dados import readMoney


while True:

    try: 
        num = readMoney("Digita: ")
        
    except(ValueError):
        print("\033[31mOps...\033[m")

    else:
        if num == -1:
            break

        # print(f"Dimuído em 13%: {diminuir(num, 13, True)}")
        # print(f"Aumentado em 10%: {aumentar(num, 10, True)}")
        # print(f"Metade: {metade(num, True)}")
        # print(f"Dobro: {dobro(num, True)}")
        # print("")
        all(num, 80, 35)
    finally:
        print("De novo!!\n")


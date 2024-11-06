def ficha (player = "<desconhecido>", gols = "0"):
    if player.isalpha() is not True:
        player = "<desconhecido>"
    if gols.isnumeric() is not True:
        gols = 0
    print("O jogador {} fez {} gol(s) no campeonato!" .format(player, gols))

    
player = str(input("Nome do jogador: "))
gols = str(input("Gols: "))

ficha(player, gols)

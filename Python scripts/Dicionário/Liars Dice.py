from random import randint
game = {'jogador1':'-', 'jogador2':'-', 'jogador3':'-', 'jogador4':'-'}

for pos, c in game.items():
    game[pos] = randint(1, 6) 

print(game)

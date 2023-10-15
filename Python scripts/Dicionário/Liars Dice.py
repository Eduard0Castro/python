from random import randint
from operator import itemgetter

game = {'jogador 1':'-', 'jogador 2':'-', 'jogador 3':'-', 'jogador 4':'-'}

for pos, c in game.items():
    game[pos] = randint(1, 6) 
    print(f"{pos} tirou {game[pos]}")
print("")
print(game)

#game aqui passa a ser uma lista:
game = sorted(game.items(), key=itemgetter(1), reverse=True)

print(game)

for i in range (0, len(game)):
    print(f"O {game[i][0]} com {game[i][1]}")
print("")
for c in game:
    print(f"O {c[0]} com {c[1]}")
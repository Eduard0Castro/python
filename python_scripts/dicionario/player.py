players = []
inter = {}

while True:

    inter['Nome'] = str(input("Digite o nome do jogador: "))
    inter['Partidas'] = int(input("Quantas partidas esse jogador jogou? "))
    inter['Goals'] = []
    soma = 0 
    for i in range (0, inter['Partidas']):
        inter['Goals'].append(int(input("Digite quantos gols {} fez na {}ª partida: "
                                      .format(inter['Nome'], i + 1))))
        soma += inter['Goals'][i]

    inter['Total'] = soma

    players.append(inter.copy())
    c = ""
    
    while c != 'N' and c != 'S':
        c = str(input("Quer continuar? [S/N]: ")).upper()

    if c == 'N':
        break

print(players)
print("")
for pos, j in enumerate(players):
    print(f"{pos:<2} {j['Nome']:<5} ", f"{j['Goals']}",f"{j['Total']:>10}")

while True:
    print("")
    jog = int(input("Quer ver os dados de qual jogador? (-1 para sair!): "))
    if jog == -1:
        break
    for r in range(0, players[jog]['Partidas']):
        print(f"Na {r + 1}ª partida o jogador {players[jog]['Nome']} marcou {players[jog]['Goals'][r]}")

    
player = {}
player['Nome'] = str(input("Digite o nome do jogador: "))
player['Partidas'] = int(input("Quantas partidas esse jogador jogou? "))
player['Goals'] = []
soma = 0 
for i in range (0, player['Partidas']):
    player['Goals'].append(int(input("Digite quantos gols {} fez na {}ª partida: "
                                      .format(player['Nome'], i + 1))))
    soma += player['Goals'][i]
    
player['Total'] = soma
print(player)

print(f"\nO jogador {player['Nome']} jogou {player['Partidas']} partidas.")
for i in range (0, player['Partidas']):
    print(f"Na {i+1}ª partida ele guardou {player['Goals'][i]}")

print(f"Concluindo o campeonato com um total de {player['Total']} gols!")
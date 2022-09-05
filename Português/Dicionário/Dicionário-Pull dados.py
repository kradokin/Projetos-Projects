time = []
pontos = []
dic = {}
mais = ' '
while mais not in 'Nn':
    dic.clear()
    dic['NOME'] = input('Nome do jogador? ').title()
    quantidade = int(input(f'Quantas partidas {dic["NOME"]} jogou? '))
    pontos.clear()
    for qnt in range(quantidade):
        pontos.append(int(input(f'    Pontos na partida {qnt+1}: ')))
    dic['PONTUAÇÃO'] = pontos[:]
    dic['TOTAL'] = sum(pontos)
    time.append(dic.copy())
    mais = input('Continuar? [S/N] ')
print('='*48)
print('<<RESULTADO>>')
print('Cod.', end='')
for key in dic.keys():
    print(f'{key:<15}', end='')
print()
print('-'*48)
for k, v, in enumerate(time):
    print(f'{k} ', end='')
    for val in v.values():
        print(f'{str(val):<15}', end=' ')
    print()
print()
while True:
    dados = int(input('Qual jogador deseja mostrar os dados [Cod.]? [999 para] '))
    if dados == 999:
        break
    if dados >= len(time):
        print('ERRO! Código de jogador não existe.')
    else:
        print(f'---- LEVANTAMENDO DO JOGADOR {time[dados]["NOME"]} ----')
        for i, p in enumerate(time[dados]['PONTUAÇÃO']):
            print(f'Na partida {i+1} fez {p} ponto(s)')

import random
from names import get_first_name
pontos = []
time = []
dic = {}
mais = ' '
while mais not in 'Nn':
    dic.clear()
    dic['Nome'] = get_first_name()
    print(f'Nome: {dic["Nome"]}')
    print(f'Quantas partidas {dic["Nome"]} jogou? ', end='')
    partidas = random.randint(0, 5)
    print(partidas)
    pontos.clear()
    for qnt in range(partidas):
        print(f'     Pontos na partida {qnt+1}: ', end='')
        ponto = random.randint(0, 9)
        pontos.append(ponto)
        print(ponto)
    dic['Pontuação'] = pontos[:]
    dic['Total'] = sum(pontos)
    time.append(dic.copy())
    mais = input('Continuar? ')
print(f'\nCod.', end=' ')
for k in dic.keys():
    print(f'{k:<16}', end='')
print()
for k, v in enumerate(time):
    print(f'{k}  ', end='')
    for val in v.values():
        print(f'{str(val):<16}', end=' ')
    print()
while True:
    dados = int(input('Dados do jogador: [digite o cod.] '))
    if dados == -1:
        break
    if dados >= len(time):
        print('Erro! Digite o código correto.')
    else:
        print(f'-------- LEVANTAMENDO DO JOGADOR {time[dados]["Nome"]} --------')
        for i, p in enumerate(time[dados]['Pontuação']):
            print(f'Na partida {i+1} fez {p} ponto(s)')

# Dictionary-Pool of information
# Project to search information about a player
import random
from names import get_first_name
pontos = []  # The points
time = []  # The team
dic = {}  # The dictionary
mais = ' '  # Answere if Y or N. Line 25
while mais not in 'Nn':
    dic.clear()
    dic['Name'] = get_first_name()
    print(f'Name: {dic["Name"]}')
    print(f'How many games did {dic["Name"]} play? ', end='')
    partidas = random.randint(0, 5)
    print(partidas)
    pontos.clear()
    for qnt in range(partidas):
        print(f'     points in the match {qnt+1}: ', end='')
        ponto = random.randint(0, 9)
        pontos.append(ponto)
        print(ponto)
    dic['Points'] = pontos[:]
    dic['Total'] = sum(pontos)
    time.append(dic.copy())
    mais = input('Continue? ')
print(f'\nCode', end=' ')
for k in dic.keys():
    print(f'{k:<16}', end='')
print()
for k, v in enumerate(time):
    print(f'{k}  ', end='')
    for val in v.values():
        print(f'{str(val):<16}', end=' ')
    print()
while True:
    dados = int(input('Player data: [enter code] '))
    if dados == -1:
        break
    if dados >= len(time):
        print('Error! Enter the correct code.')
    else:
        print(f'-------- PLAYER LIFTING {time[dados]["Name"]} --------')
        for i, p in enumerate(time[dados]['Points']):
            print(f'In the game {i+1} scored {p} point(s)')

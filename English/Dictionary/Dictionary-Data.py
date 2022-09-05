# Dictionary-Dice
# Project to roll a dice.
from random import randint
from operator import itemgetter
rodada = {}  # The round
lista = []  # The list
for c in range(4):
    rodada[f'Player {c+1}'] = randint(1, 6)
for k, v in rodada.items():
    print(f'The {k} rolled {v}')
lista.append(rodada.copy())
ranking = sorted(rodada.items(), key=itemgetter(1), reverse=True)
for pos, num in enumerate(ranking):
    print(f'{pos+1}º position: {num[0]} with {num[1]} points')

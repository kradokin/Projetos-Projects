from random import randint
from operator import itemgetter
rodada = {}
lista = []
for c in range(4):
    rodada[f'Jogador {c+1}'] = randint(1, 6)
for k, v in rodada.items():
    print(f'O {k} tirou {v}')
lista.append(rodada.copy())
ranking = sorted(rodada.items(), key=itemgetter(1), reverse=True)
for pos, num in enumerate(ranking):
    print(f'{pos}º lugar: Jogador {num[0]} com {num[1]}')

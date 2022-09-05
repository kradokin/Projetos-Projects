# Dictionary-Player
# Project to register all the points of a player's match
lista = []  # The list
dic = {}  # The dictionary
tot = 0  # Total
while True:
    dic['NAME'] = input("Player's name? ").title()
    quantas = int(input(f'How many matches {dic["NAME"]} played? '))
    for qnt in range(quantas):
        pont = int(input(f'     How many points in the game {qnt+1}? '))
        lista.append(pont)
        tot += pont  # To sum the points
        dic['POINTS'] = lista
        dic['TOTAL'] = tot
    break
print('='*20)
print(dic)
print('='*20)
for k, v, in dic.items():
    print(f'The field {k} receives {v}')
print('='*20)
print(f'Player {dic["NAME"]} played {quantas} games')
for g, f in enumerate(lista):
    print(f'    =>In the {g+1}º game, he scored {f} points')

lista = []
dic = {}
tot = 0
while True:
    dic['NOME'] = input('Nome do jogador? ').title()
    quantas = int(input(f'Quantas partidas {dic["NOME"]} jogou? '))
    for qnt in range(quantas):
        pont = int(input(f'     Quantos pontos na partida {qnt+1}? '))
        lista.append(pont)
        tot += pont
        dic['PONTUAÇÃO'] = lista
        dic['TOTAL'] = tot
    break
print('='*20)
print(dic)
print('='*20)
for k, v, in dic.items():
    print(f'O campo {k} recebe {v}')
print('='*20)
print(f'O jogador {dic["NOME"]} jogou {quantas} partidas')
for g, f in enumerate(lista):
    print(f'    =>Na partida {g+1}, fez {f} pontos')

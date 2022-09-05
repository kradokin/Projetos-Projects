def ficha(nome='<DESCONHECIDO>', pts=0):
    print(f'O jogador {nome} fez {pts} pontos no campeonato!')


n = (str(input('Nome: ')))
p = str(input('Pontos: '))
if p.isnumeric():
    p = int(p)
else:
    p = 0
if n.strip() == '':
    ficha(pts=p)
else:
    ficha(n, p)

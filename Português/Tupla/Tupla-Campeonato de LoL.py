classificação = ('DWG KIA', 'Cloud9', 'Rogue', 'FunPlus Phoenix', 'T1',
                 'EDward Gaming', '100 Thieves', 'DetonatioN FocusMe',
                 'Royal Never Give Up', 'Hanwha Life', 'PSG Talon', 'Fnatic',
                 'Gen.G', 'MAD Lions', 'LNG Esports', 'Team Liquid')

print(f'Total de times classificados: {len(classificação)}')
print(f'Os cinco primeiros classificados foram: {classificação[0:5]}')
print(f'Os últimos quatro classificados foram: {classificação[-4:]}')
print(f'Os times em ordem alfabética: {sorted(classificação)}')
cl = int(input('Para saber a classificação do time, digite o número: '))
while cl not in range(0, 16):
    cl = int(input('Classificação entre 0 e 15, digite o número: '))
    if cl in range(0, 16):
        break
print(f'O time {classificação[cl-1]} ficou na {cl}ª colocação e atrás de {classificação[:cl-1]}')


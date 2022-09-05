from random import randint
import time
lista = []
jogos = []
total = 1
qnt = int(input('Quantas jogadas? '))
while total <= qnt:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'      SORTEANDO {qnt} LISTAS      ')
for i, l in enumerate(jogos):
    time.sleep(0.5)
    print(f'{i+1}º sorteio: {l}')

from time import sleep


def contagem(i, f, p):
    print('-'*20)
    print(f'Contagem de {i} a {f} de {p} em {p}')
    print('='*20)
    if i < f:
        count = i
        while count <= f:
            print(f'{count}', end=' ', flush=True)
            sleep(0.5)
            count += p
        print('FIM')
    else:
        count = i
        while count >= f:
            print(f'{count}', end=' ', flush=True)
            sleep(0.5)
            count -= p
    print()
    print('='*20)


contagem(1, 10, 1)
contagem(10, 0, 2)
print('CONTAGEM PERSONALIZADA:')
contagem(i = int(input('Início: ')), f = int(input('Final: ')), p = int(input('Passo: ')))

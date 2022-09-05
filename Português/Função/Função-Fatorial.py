def fatorial(a, b=False):
    '''
    -> Programa calcula fatorial de qualquer número
    :param a: Número escolhido
    :param b: False: Mostra somente o resultado; True: Mostra o passo a passo
    :return: retorna 1
    '''
    f = 1
    for c in range(a, 0, -1):
        if b:
            print(c, end='')
            if c > 1:
                print(' x', end=' ')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(int(input('Fatorial do número ')), True))

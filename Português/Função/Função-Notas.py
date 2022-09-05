import math


def notas(*resp, sit=False):
    '''
    -> O programa lê a quantidade de notas e mostra o Total de notas (n quantidade), Maior nota, Menor nota e a Média simples. Além da situação: sit=True
    :param resp: Todas as notas a serem analizadas;
    :param sit: Mostra ou não a situação com base na média;
    :return: Sem retorno.
    '''
    med = sum(resp) / len(resp)
    print(f'Total de {len(resp)} notas; Maior: {max(resp)}; Menor: {min(resp)}; Média: {med:.3f}', end='')
    if sit:
        print('; Situação: ', end='')
        if med <= 5.9:
            print('RUIM')
        if 6 <= med <= 8.9:
            print('REGULAR')
        if med >= 9:
            print('EXCELENTE')


resp = notas(8.3, 8.8, 10, sit=True)

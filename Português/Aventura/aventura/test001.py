from aventura_txt import *


welcome()


def right_left():
    try:
        answer01 = input('Direita ou Esquerda? ')
    except:
        print('Digite Direita ou Esquerda')
    else:
        if answer01 == 'direita'.lower():
            print()
            print(right)
            print()
        if answer01 == 'esquerda'.lower():
            print()
            print(left)
            print()


right_left()


def atk_run():
    try:
        answer02 = input('Atacar ou correr? ')
    except:
        print('Digite atacar ou corre.')
    else:
        if answer02 == 'atacar'.lower():
            print()
            print(atk)
            print()
        if answer02 == 'correr'.lower():
            print()
            print(run)
            print()


atk_run()

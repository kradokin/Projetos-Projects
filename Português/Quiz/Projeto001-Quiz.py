# Projeto Quiz não finalizado.
from time import sleep
print("Bem vindo ao QUIZ!")
play = str(input("Você quer jogar? ")).upper()
if play == 'SIM' or play == 'S':
    print("Vamos começar! Deve ser respondido em inglês.")
    sleep(0.5)
    print('~'*70)
    print('São 3 chances para acertar a resposta (em inglês) para cada pergunta.\n'
          'A cada resposta errada para cada pergunta subtrai-se 0.5 pontos.\n'
          '1ª chance: +2.5\n2ª chance: +2.0\n3ª chance: +1.5.')
    print('~'*70)
    sleep(1)
else:
    print('Ok! Até mais...')
    quit()


def quiz(txt):
    perg = ["O que significa CPU? ", "O que significa GPU? ",
            "O que significa RAM? ", "O que significa PSU? "]
    respcer = ['central processing unit', 'graphics processing unit',
               'random access memory', 'power supply unit']
    c_total = c_perg = c_erra = 0
    pt = 0
    while c_perg < 4:
        user = input(perg[c_perg])
        if user != respcer[c_perg].lower():
            c_erra += 1
            c_total += 1
            print('Resposta incorreta.', end=' ')
            if c_total == 3:
                c_perg += 1
                if c_perg + 1:
                    c_total = 0
                    c_erra = 0
                    print('\n')
        elif user == respcer[c_perg].lower():
            c_total = 0
            c_perg += 1
            if c_erra == 0:
                pt += 2.5
            if c_erra == 1:
                pt += 2.0
            if c_erra == 2:
                pt += 1.5
            print('Parabens!!')
            print()
            c_erra = 0
            if c_perg < 4:
                sleep(0.5)
                print('Próxima pergunta.')
                sleep(0.5)
    print(f'Você finalizou o QUIZ e obrigado por jogar.\nSua pontuação final: {pt}')


quiz('Sua resposta: ')

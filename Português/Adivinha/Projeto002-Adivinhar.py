from random import randint


def numero(nume):
    count_guesses = count_except = 0
    while True:
        try:
            num = int(input(nume))
            assert num > 0
        except AssertionError:
            print('Digite um número maior que ZERO')
        except (ValueError, TypeError):
            print('Oops! Digite um número inteiro.')
        else:
            if num > 0:
                print(f'Boa! Agora tente adivinhar o número entre 1 e {num}. Boa sorte!')
                random_num = randint(1, num)
                while True:
                    try:
                        guess_user = int(input('Adivinhe o número: '))
                        assert guess_user > 0
                        assert guess_user < num+1
                    except AssertionError:
                        print(f'Digite um número entre 1 e {num}')
                        count_except += 1
                    except (ValueError, TypeError):
                        print('Oops! Digite um número inteiro.')
                        count_except += 1
                    else:
                        count_guesses += 1
                        if guess_user != random_num:
                            if guess_user < random_num:
                                print('Chute para cima.', end=' ')
                            if guess_user > random_num:
                                print('Chute para baixo.', end=' ')
                        if guess_user == random_num:
                            print(f'Você acertou em {count_guesses} palpite(s), '
                                  f'e com {count_except} palpite(s) fora da curva')
                            print('Obrigado por jogar!!!')
                            break
            break


numero('Digite um número: ')

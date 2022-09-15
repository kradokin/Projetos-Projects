from random import randint


def numero(nume):
    count_guesses = count_except = 0
    while True:
        try:
            num = int(input(nume))
            assert num > 0
        except AssertionError:
            print('Please type a number larger than 0 next time.')
        except (ValueError, TypeError):
            print('Oops! Please type a number next time.')
        else:
            if num > 0:
                print(f'Nice! Now try to guess the number between 1 and {num}. Good luck!')
                random_num = randint(1, num)
                while True:
                    try:
                        guess_user = int(input('Make a guess: '))
                        assert guess_user > 0
                        assert guess_user < num+1
                    except AssertionError:
                        print(f'Type a numbe between 1 and {num}')
                        count_except += 1
                    except (ValueError, TypeError):
                        print('Oops! Please type a number next time.')
                        count_except += 1
                    else:
                        count_guesses += 1
                        if guess_user != random_num:
                            if guess_user < random_num:
                                print('You were below the number!', end=' ')
                            if guess_user > random_num:
                                print('You were above the number!', end=' ')
                        if guess_user == random_num:
                            print(f'You got it in {count_guesses} guess(es), '
                                  f'and there were {count_except} outside the curve guess(es).')
                            print('Thanks for playing!!!')
                            break
            break


numero('Type a number: ')

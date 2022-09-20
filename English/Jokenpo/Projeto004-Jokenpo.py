import random

count = 0
options = ['Rock', 'Paper', 'Scissors']
print('Choose an option to play Jokenpo.')

for x in zip(options):
    print(f'{count} - {x[0]}')
    count += 1
print()


def rules():
    each_round = pc_win = player_win = tie = 0
    rounds = int(input('How many games do you want to play? '))
    while each_round < rounds:
        try:
            print(f'ROUND {each_round + 1}'.center(30))
            player_chose = int(input('Your play: '))
            assert player_chose < 3
            each_round += 1
        except (ValueError, TypeError, AssertionError):
            print('Please, type [0], [1] or [2]\n')
        except KeyboardInterrupt:
            print('\nThanks for playing!')
            quit()
        else:
            pc_chose = random.choice(options)
            if options[player_chose] == pc_chose:
                tie += 1
                print(f'You played: {options[player_chose]}')
                print(f'The computer played: {pc_chose}')
            if options[player_chose] != pc_chose:
                if (options[player_chose] == options[0] and pc_chose == options[2]) or \
                        (options[player_chose] == options[2] and pc_chose == options[1]) or \
                        (options[player_chose] == options[1] and pc_chose == options[0]):
                    player_win += 1
                    print(f'You played: {options[player_chose]}')
                    print(f'The computer played: {pc_chose}')
                else:
                    pc_win += 1
                    print(f'You played: {options[player_chose]}')
                    print(f'The computer played: {pc_chose}')
            print()
    print('\nEnd game! Results')
    print(f'{tie} tie(s)\nYou won {player_win} game(s)\nThe computer won {pc_win} game(s)')


rules()

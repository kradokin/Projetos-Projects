import random

count = 0
options = ['PEDRA', 'PAPEL', 'TESOURA']
print('Escolha uma opção para jogar Jokenpô.')

for x in zip(options):
    print(f'{count} - {x[0]}')
    count += 1
print()


def rules():
    each_round = pc_win = player_win = tie = 0
    rounds = int(input('Quantas partidas deseja jogar? '))
    while each_round < rounds:
        try:
            print(f'PARTIDA {each_round + 1}'.center(30))
            player_chose = int(input('Sua escolha: '))
            assert player_chose < 3
            each_round += 1
        except (ValueError, TypeError, AssertionError):
            print('Por favor, digite [0], [1] ou [2]\n')
        except KeyboardInterrupt:
            print('\nObrigado por jogar!')
            quit()
        else:
            pc_chose = random.choice(options)
            if options[player_chose] == pc_chose:
                tie += 1
                print(f'Você escolheu: {options[player_chose]}')
                print(f'O computador escolheu: {pc_chose}')
            if options[player_chose] != pc_chose:
                if (options[player_chose] == options[0] and pc_chose == options[2]) or \
                        (options[player_chose] == options[2] and pc_chose == options[1]) or \
                        (options[player_chose] == options[1] and pc_chose == options[0]):
                    player_win += 1
                    print(f'Você escolheu: {options[player_chose]}')
                    print(f'O computador escolheu: {pc_chose}')
                else:
                    pc_win += 1
                    print(f'Você escolheu: {options[player_chose]}')
                    print(f'O computador escolheu: {pc_chose}')
            print()
    print('\nFim do jogo! Resultado')
    print(f'Ao todo, {tie} empate(s)\nVocê ganhou {player_win} partida(s)\nO computador ganhou {pc_win} partida(s)')


rules()


name = input('Olá aventureiro(a)! Como o posso chamar? ').title()
classes = {'1': 'Paladino(a)',
           '2': 'Guerreiro(a)',
           '3': 'Caçador(a)',
           '4': 'Mago(a)',
           '5': 'Bruxo'}
skills = {'1': 'Luz Sagrada',
          '2': 'Investida',
          '3': 'Tiro Firme',
          '4': 'Chuva de Gelo',
          '5': 'Invocar Diabrete'}
for k, v in enumerate(classes.values()):
    print(f'Classe {k+1}: {v}')
class_ = (input('Por favor, escolha sua classe: '))


def welcome():

    for key, value in zip(classes, class_):
        print(f'Seja muito bem vindo(a) a AVENTURA CINCO VIDAS, {classes[value]} {name}!')
        print()
        print('Dizem que nossos dias começam quando ganhamos o Selo dos Castores.\n'
              f'Sua aventura começa quando você, {name}, ganha o Título de Classe {classes[value]} '
              f'na academia Bons Castores,\num colegial feito para quem deseja trilhar caminhos desconhecidos...')
    print()
    print('Dia sete: O início')
    print('Caminhando em uma trilha com seus equipamentos em uma mochila na Floresta da Mancha, '
          'com vários barulhos a sua esquerda\nvocê encontra uma bifurcação logo a sua frente e '
          'terá que decidir qual caminho deve tomar.')


right = 'Você continua em direção ao Vale dos Mortos e repara que está muito silêncioso, ' \
          'até que você percebe que estava\nsendo seguido desde por 14 ninjas que cambaleavam' \
          'e partem para cima de você com tudo.'
left = 'Você continua em direção ao Caminho 7 ventos em meio ao barulho. A cada passo, ' \
           'o barulho aumentava, até que depois de\n5 minutos caminhando você não aguenta mais ' \
           'o barulho e entra na mata para identificar\n e cessar o chiado custe o que custar. Então depois' \
           'de 4 minutos e 20 segundos você começa a perceber\n uma realidade distorcida, sua visão ' \
           'começa a distorcer, você fica confuso e não aguenta...\ncai no chão e é nocauteado.'

for key, value in zip(skills, class_):
    atk = f'Com a sabedoria que lhe foi ensinado(a) na academia Bons Castores, você utiliza a habilidade {skills[value]}'\
          f'para derrota-los um a um e assim que feito,\nvocê se direciona ao lider deles.'
run = 'Você não deseja arriscar sua vida desse jeito, como dizia o Mestre Fanc "É preferível correr e esconder do que enfrentar' \
      'o inimigo com vantagem" e assim você fez.\nDepois de 10 minutos correndo sem olhara para trás, você parou' \
      'e tirou de sua mochila um frasco de estâmina, assim você poderia correr por mais 15 minutos. Enquanto corria' \
      'você lembrava que Mestre Franc, na verdade,\nera um discípulo que se achava mestre, mas sempre fugia das lutas de classe.'

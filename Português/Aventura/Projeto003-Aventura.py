#WARNING!!! IN PROGRESS
#ATENÇÃO!!! EM PROGRESSO

name = input('Olá aventureiro(a)! Como o posso chamar? ').title()
classes = {'1': 'Paladino(a)',
           '2': 'Guerreiro(a)',
           '3': 'Caçador(a)',
           '4': 'Mago(a)',
           '5': 'Druida'}
for k, v in enumerate(classes.values()):
    print(f'Classe {k+1}: {v}')
class_ = (input('Por favor, escolha sua classe: '))

for key, value in zip(classes, class_):
    print(f'Seja muito bem vindo(a) a AVENTURA CINCO VIDAS, {classes[value]} {name}!')
    print()
    print('Dizem que nossos dias começam quando ganhamos o Selo dos Castores.\n'
          f'Sua aventura começa quando você, {name}, ganha o Título de Classe {classes[value]} na academia BONS CASTORES,\n'
          'um colegial feito para quem deseja trilhar caminhos desconhecidos.')
print()
print('Dia sete: O início')
answer = input('Caminhando em uma trilha com seus equipamentos em uma mochila floresta escura, '
               'com vários barulhos a sua esquerda você encontra uma bifurcação logo a sua frente')

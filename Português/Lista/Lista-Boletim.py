dados = []
resp = ' '
med = 0
while resp not in 'Nn':
    nome = (input('Nome: ')).title()
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    resp = input('Deseja continuar? [S/N] ')
print('=-='*10)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for pos, a in enumerate(dados):
    print(f'{pos:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-'*25)

while True:
    qual = int(input('Mostrar nota de qual aluno? (*none* INTERROMPE) '))
    if qual == 999:
        break
    if qual <=len(dados) - 1:
        print(f'As notas de {dados[qual][0]} foram {dados[qual][1]}')

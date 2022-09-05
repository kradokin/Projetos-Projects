aluno = {}
for a in range(1):
    aluno['Nome'] = input('Nome: ').title()
    aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Media'] > 5:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

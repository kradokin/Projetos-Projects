dic = {}
lista = []
totida = 0
while True:
    dic['nome'] = input('Nome: ').title()
    dic['sexo'] = input('Sexo: [M/F] ').upper()
    while dic['sexo'] not in 'MmFf':
        dic['sexo'] = input('ERRO! Por favor, digite apenas M ou F. ').upper()
    dic['idade'] = int(input('Idade: '))
    totida += dic['idade']
    mais = input('Continuar? [S/N] ').upper()
    while mais not in 'SsNn':
        mais = input('ERRO! Responda apenas S ou N. ').upper()
    lista.append(dic.copy())
    media = totida / len(lista)
    if mais in 'Nn':
        break
print(f'A) Ao todo, temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for pessoa in lista:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=' ')
print()
print(f'D) Lista de pessoas que estão acima da média:')
for pessoa in lista:
    if pessoa['idade'] > media:
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\n >> CADASTRO ENCERRADO << ')

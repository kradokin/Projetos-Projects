dados = []
lista = []
resp = ' '
maior = menor = 0
while resp not in 'Nn':
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    resp = input('Deseja continuar? [S/N] ')
print(f'AO TODO, foram {len(lista)} pessoa(s) cadastradas')
print(f'O MAIOR peso cadastrado foi de {maior}kg', end=' ')
for pessoa in lista:
    if pessoa[1] == maior:
        print(f'{pessoa[0].title()}', end=' ')
print()
print(f'O MENOR peso cadastrado foi de {menor}kg', end=' ')
for pessoa in lista:
    if pessoa[1] == menor:
        print(f'{pessoa[0].title()}', end=' ')
print()
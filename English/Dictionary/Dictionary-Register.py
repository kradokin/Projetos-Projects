# Dictionary-Register
# Project to register names and ages
dic = {}  # The dictionary
lista = []  # The list
totida = 0  # Total age
while True:
    dic['name'] = input('Name: ').title()
    dic['sex'] = input('Sex: [M/F] ').upper()
    while dic['sex'] not in 'MmFf':
        dic['sex'] = input('ERROR! Please, type M or F. ').upper()
    dic['age'] = int(input('age: '))
    totida += dic['age']  # To sum all age
    mais = input('Continue? [Y/N] ').upper()
    while mais not in 'YyNn':  # In case of someone answere 'mais' wrong
        mais = input('ERROR! Answere only Y or N. ').upper()
    lista.append(dic.copy())
    media = totida / len(lista)
    if mais in 'Nn':
        break
print(f'A) In all, we have {len(lista)} people registered.')
print(f'B) The average age is {media:.2f} years.')
print(f'C) The registered women were: ', end='')
for pessoa in lista:  # For each woman registered in list
    if pessoa['sex'] == 'F':
        print(pessoa['name'], end=' ')
print()
print(f'D) List of people who are above average:')
for pessoa in lista:  # For each person
    if pessoa['age'] > media:
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\n >> REGISTRATION CLOSED << ')

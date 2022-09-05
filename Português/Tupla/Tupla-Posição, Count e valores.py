count = 1
maior = menor = 0
n = (int(input('Numero: ')),
    int(input('Numero: ')),
    int(input('Numero: ')),
    int(input('Numero: ')))
print(f'A Tupla constitui de {n}')
print(f'O número 9 apareceu {n.count(9)} vez(es)')
if 3 in n:
    print(f'O número 3 apareceu na {n.index(3)+1}ª posição')
else:
    print(f'O valor 3 não apareceu nessa tupla')
print(f'O valores pares digitados foram', end=' ')
for par in n:
    if par % 2 == 0:
        print(par, end=' ')


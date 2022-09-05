from random import randint
from random import sample
rand = tuple(sample(range(10), 5))
print('Os valores sorteados foram: ', end='')
print(rand)
#METODO ANTIGO DE MAIOR E MENOR
'''count = 0
maior = menor = 0
while count < 5:
    rand = randint(1, 10)
    count += 1
    if count == 1:
        maior = menor = rand
    else:
        if maior > rand:
            maior = rand
        elif menor < rand:
            menor = rand
    print(rand, end=' ')'''
#print(f'\nO MENOR valor foi {maior}\nO MAIOR valor foi {menor}')
#NOVO METODO DE MAIOR/MAX E MENOR/MIN
print(f'\nO MENOR valor foi {min(rand)}\nO MAIOR valor foi {max(rand)}')
from random import randint
lista = []
def valores(num):
    print('=-='*10)
    print('Analisando os valores...')
    print(lista, end=' ')
    print(f'Foram analisados {n+1} valores ao todo')
    print(f'O maior valor encontrado foi {max(lista)}')


for n in range(6):
    valor = (randint(0, 9))
    lista.append(valor)
valores(lista)
lista.clear()
for n in range(3):
    valor = (randint(0, 9))
    lista.append(valor)
valores(lista)

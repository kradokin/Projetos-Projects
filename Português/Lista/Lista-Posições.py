
lista = []
for count in range(5):
    num = (int(input('Digite um número: ')))
    lista.append(num)
    for pos, val in enumerate(lista):
        n = sorted(lista)
        if pos == 0:
            print(f'O número {n[pos]} foi adicionado na posição {pos}')
        if pos == 1:
            print(f'O número {n[pos]} foi adicionado na posição {pos}')
        if num > lista[len(lista)-1]: #lista[-1]
            print(f'O número {n[pos]} foi adicionado na posição final')
print(sorted(lista))

#----------------------------------------------------------------------#
'''
lista = []
for count in range(5):
    num = int(input('Digite um número: '))
    if count == 0 or num > lista[-1]:
        lista.append(num)
        print(f'Adicionado na posição final')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Valor {lista} adicionado na posição {pos}')
                break
            pos += 1
print(f'A ordem dos valores digitados: {lista}')
'''
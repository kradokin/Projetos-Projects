lista = []
sino = ' '
while sino not in 'Nn':
    n = (input('Digite um valor: '))
    sino = input('Deseja continuar? [S/N] ')
    if n not in lista:
        lista.append(n)
print(*sorted(lista), sep=' ')

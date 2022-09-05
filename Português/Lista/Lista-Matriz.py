matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somac3 = maiorl2 = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Número na posição ({l,c}): '))
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if matriz[l][c]:
            somac3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
        if matriz[l][c]:
            maiorl2 = matriz[1][0], matriz[1][1], matriz[1][2]
    print()
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da 3º coluna é de {somac3}')
print(f'A soma dos valores da 2º linha é de {max(maiorl2)}')

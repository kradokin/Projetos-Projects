n = int(input('Digite um número para ser mostrar na tabuada: '))
for i in range(0, 11):
    r = i * n
    print(f'{i:2} x {n} = {r}')

def leiaInt(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite apenas um número inteiro válido.')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você digitou {n}')

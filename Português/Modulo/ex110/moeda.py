def moeda(preco=0, simb='R$'):
    return f'{simb}{preco:.2f}'.replace('.', ',')


def metade(preco=0, formato=False):
    met = preco / 2
    return met if formato is False else moeda(met)


def dobro(preco=0, formato=False):
    dob = preco * 2
    return dob if formato is False else moeda(dob)


def aumentar(preco=0, taxa=0, formato=False):
    aum = preco * (1 + taxa / 100)
    return aum if formato is False else moeda(aum)


def diminuir(preco=0, taxa=0, formato=False):
    dim = preco - (preco * taxa / 100)
    return dim if formato is False else moeda(dim)


def resumo(preco=0, taxaa=10, taxar=5):
    print('~'*20)
    print('RESUMO DO VALOR'.center(20))
    print('~'*20)
    print(f'Preço analisado: \tR${moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metado do preço: \t{metade(preco,True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')

def metade(preco=0, formato=False):
    return preco / 2 if formato is False else moeda(preco)


def dobro(preco=0, formato=False):
    return preco * 2 if formato is False else moeda(preco)


def aumentar(preco=0, formato=False):
    return preco * 1.25 if formato is False else moeda(preco)


def diminuir(preco=0, formato=False):
    if formato is False:
        return preco * 0.75
    else:
        moeda(preco)


def moeda(preco=0, simb='R$'):
    return f'{simb}{preco:.2f}'.replace('.', ',')

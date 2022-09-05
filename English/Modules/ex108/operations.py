def fraction(price=0):
    return price / 2


def double(price=0):
    return price * 2


def percentmore(price=0):
    return price * 1.25


def percentless(price=0):
    return price * 0.75


def currency(price=0, simb='R$'):
    return f'{simb}{price:.2f}'.replace('.', ',')

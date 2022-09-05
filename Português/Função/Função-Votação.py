import datetime


def voto(ano):

    anos = datetime.date.today().year - ano
    print(f'Com {anos} anos: ', end='')
    if 18 <= anos < 65:
        print('VOTO OBRIGATÓRIO')
    if 16 <= anos < 18 or anos >= 65:
        print('VOTO OPCIONAL')
    if anos < 16:
        print('NÃO VOTA')


voto(ano=int(input('Em que ano você nasceu? ')))

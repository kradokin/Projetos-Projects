def currency(price=0, simb='CAD$'):
    '''
    -> Put the simb CAD$ before the price and replace "." to ","
    :param price: Price from test.py;
    :param simb: CAD$;
    :return: Return the currency pattern.
    '''
    return f'{simb}{price:.2f}'.replace(',', '.')


def fraction(price=0, form=False):
    '''
    -> Fraction 1/2 the price.
    :param price: Price from test.py;
    :param form: Format the price to currency pattern;
    :return: Return the currency pattern.
    '''
    frac = price / 2
    return frac if form is False else currency(frac)


def double(price=0, form=False):
    '''
    -> Double the price.
    :param price: Price from test.py;
    :param form: Format the price to currency pattern;
    :return: Return the currency pattern.
    '''
    doub = price * 2
    return doub if form is False else currency(doub)


def percentmore(price=0, tax=0, form=False):
    '''
    -> Increase by percent the original price. Percentage can be changed in test.py
    :param price: Price from test.py;
    :param tax: How much the price will increase in percentage;
    :param form: Format the price to currency pattern;
    :return: Return the currency pattern.
    '''
    more = price * (1 + tax / 100)
    return more if form is False else currency(more)


def percentless(price=0, tax=0, form=False):
    '''
    -> Decrease by perent the original price. Percentage can be changed in test.py
    :param price: Price from test.py;
    :param tax: How much the price will decrease in percentage;
    :param form: Format the price to currency pattern;
    :return: Return the currency pattern.
    '''
    less = price - (price * tax / 100)
    return less if form is False else currency(less)


def sumary(price=0, taxm=10, taxl=5):
    print('~'*20)
    print('SUMMARY OF VALUE'.center(20))
    print('~' * 20)
    print(f'Price analyzed: \t{currency(price)}')
    print(f'Double the price: \t{double(price, True)}')
    print(f'1/2 the price: \t\t{fraction(price, True)}')
    print(f'{taxm}% of increase: \t{percentmore(price, taxm, True)}')
    print(f'{taxl}% of reduction: \t{percentless(price, taxl, True)}')

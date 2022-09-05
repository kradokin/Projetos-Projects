from ex107 import operations

p = float(input('Enter the price: R$'))
print(f'1/2 of {p} is {operations.fraction(p)}')
print(f'Double of {p} is {operations.double(p)}')
print(f'125% of {p} is {operations.percentmore(p)}')
print(f'75% of {p} is {operations.percentless(p)}')

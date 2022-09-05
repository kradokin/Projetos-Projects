from ex108 import operations

p = float(input('Enter the price: R$'))
print(f'1/2 of {operations.currency(p)} is {operations.currency(operations.fraction(p))}')
print(f'Double of {operations.currency(p)} is {operations.currency(operations.double(p))}')
print(f'125% of {operations.currency(p)} is {operations.currency(operations.percentmore(p))}')
print(f'75% of {operations.currency(p)} is {operations.currency(operations.percentless(p))}')

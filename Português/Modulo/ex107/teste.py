from moeda import metade, dobro, aumentar, diminuir
from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'125% de {moeda(p)} é {moeda(aumentar(p))}')
print(f'75% de {moeda(p)} é {moeda(diminuir(p))}')

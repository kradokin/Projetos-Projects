from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'125% de {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p))}')
print(f'75% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p))}')

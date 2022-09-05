pal = ("APRENDER", "PROGRAMA", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS", "ESTUDAR", "PRATICAR", "TRABALHAR",
        "MERCADO", "PROGRAMADOR", "FUTURO")
for pos in pal:
    print(f'\nNa palavra {pos}, temos ', end='')
    for vog in pos:
        if vog.lower() in 'aeiou':
            print(f'{vog}', end=' ')

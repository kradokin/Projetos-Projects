def leiadin(txt):
    valido = False
    while not valido:
        entrada = str(input(txt)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro! \"{entrada.upper()}\" é um preço inválido.\033[m')
        else:
            valido = True
            return float(entrada)

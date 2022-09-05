def manual(txt):
    titulo(f'Acessando o manual do comando {txt}')
    help(txt)
def titulo(msg):
    tam = len(msg) + 4
    print(f' {msg}')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou comando > '))
    if comando.upper() == 'FIM':
        break
    else:
        manual(comando)
titulo('ATÉ LOGO!')
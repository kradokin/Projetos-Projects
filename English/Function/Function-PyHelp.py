# Function-Help System
# Project show python help system
def manual(txt):
    title(f'Python manual: {txt}')
    help(txt)
def title(msg):
    tam = len(msg) + 4
    print(f' {msg}')

command = ''
while True:
    title('PyHELP HELP SYSTEM')
    command = str(input('function or command > '))
    if command.upper() == 'THE END':
        break
    else:
        manual(command)
title('ATÉ LOGO!')

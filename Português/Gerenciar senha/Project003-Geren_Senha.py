from cryptography.fernet import Fernet
# Necessário rodar uma única vez o def w_encrypt() para gerar a chave encriptada
'''
def w_encrypt():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as encrypt:
        encrypt.write(key)
'''


def l_encrypt():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = l_encrypt()
fer = Fernet(key)


def add():
    account = input('Nome da conta: ').title()
    pwd = input('Senha: ')
    with open('password.txt', 'a') as f:
        f.write(account + ';' + fer.encrypt(pwd.encode()).decode() + '\n')


def view():
    with open('password.txt', 'r') as f:
        for each_line in f.readlines():
            data = each_line.rstrip()
            user, pword = data.split(';')
            print(f'Usuário: {user} ; Senha: {fer.decrypt(pword.encode()).decode()}')


while True:
    new_view = input('Você gostaria de adicionar uma nova senha ou visualizar as existentes?\n'
                     '[1 - Adicionar / 2 - Visualizar / 3 - Sair]: ')
    if new_view == '3':
        print('Obrigado por utilizar nosso Gerenciamento de Senha!')
        quit()
    if new_view == '1':
        add()
    elif new_view == '2':
        view()
    else:
        new_view = input('Digite uma opção válida: ')
        continue

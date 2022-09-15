from cryptography.fernet import Fernet
# You only need to run def w_encrypt() once to generate the encrypted key
'''
def w_encrypt():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as encrypt:
        encrypt.write(key)
w_encrypt()
'''


def l_encrypt():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = l_encrypt()
fer = Fernet(key)


def add():
    account = input('Account name: ').title()
    pwd = input('Password: ')
    with open('data.txt', 'a') as f:
        f.write(account + ';' + fer.encrypt(pwd.encode()).decode() + '\n')


def view():
    with open('data.txt', 'r') as f:
        for each_line in f.readlines():
            data = each_line.rstrip()
            user, pword = data.split(';')
            print(f'User: {user} ; Password: {fer.decrypt(pword.encode()).decode()}')
    print()


while True:
    new_view = input('Would you like to add a new password or view existing ones?\n'
                     '[1 - Add / 2 - View / 3 - Quit]: ')
    if new_view == '3':
        print('Thank you for using our Password Management!')
        quit()
    if new_view == '1':
        add()
    elif new_view == '2':
        view()
    else:
        print('Please enter a valid option: ')
        continue

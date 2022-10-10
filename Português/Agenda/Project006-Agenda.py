# Simple agenda with functionalities to add, view, delete, search and change (soon) contacts
# This is not the finished project and I will change it as soon as possible.
def save_contact(list_of_contact):
    with open('data.txt', 'w+') as file:
        for contact in list_of_contact:
            file.write(contact['name'] + '|' + contact['note'] + '|' + contact['email'] + '|' + contact['phone'] + '\n')


def load_contact():
    list_of_all_contacts = []
    try:
        with open('data.txt', 'r') as file:
            for each_line in file.readlines():
                column = each_line.strip().split('|')
                contact = {
                    'name': column[0],
                    'note': column[1],
                    'email': column[2],
                    'phone': column[3]
                }
                list_of_all_contacts.append(contact)
        if file:
            with open('data.txt', 'w+') as file:
                file.write()
    except FileNotFoundError:
        print(f'Error. File {file} not found')
    else:
        return list_of_all_contacts


def exist_email(agenda, email):
    if len(agenda) > 0:
        for contact in agenda:
            if contact['email'] == email:
                return True
    return False


def add_contact(agenda):
    while True:
        email = input('E-mail: ')
        if not exist_email(agenda, email):
            break
        else:
            print('Email already exist.')
    contact = {
        'email': email,
        'name': input('Name: '),
        'note': input('Note: '),
        'phone': input('Phone: ')
    }
    agenda.append(contact)
    print(f'Information about {contact["name"]} added')


def search_contact(agenda):
    if len(agenda) > 0:
        print('===== CONTACT FINDER ====='.center(20))
        options = str(input('Find a contact by\n[1] Name\n[2] Note\n[3] Email\n[4] Phone\n>> '))
        find_by = {'1': 'name',
                   '2': 'note',
                   '3': 'email',
                   '4': 'phone'
                   }
        try:
            to_be_found = str(input(f'{find_by[options].title()} to be found: '))
        except:
            print('Does not exist')
        else:
            count = 0
            for contact in agenda:
                if contact[find_by[options]] == to_be_found.lower():
                    print(f'>')
                    print(f'\tName: {contact["name"].title()}')
                    print(f'\tNote: {contact["note"]}')
                    print(f'\tE-mail: {contact["email"]}')
                    print(f'\tPhone: {contact["phone"]}')
                    count += 1
            print('Found', count, 'user(s)')
            print('=' * 20)


def change_contact(agenda):  # To be finished
    '''
    if len(agenda) > 0:
        print('===== CHANGE CONTACT ====='.center(20))
        options = int(input('Find a contact by\n[1] Name\n[2] Note\n[3] Email\n[4] Phone\n>> '))
        find_by = {1: 'name',
                   2: 'note',
                   3: 'email',
                   4: 'phone'
        }
        with open('data.txt', 'r') as file:
            to_be_found = str(input(f'{find_by[options].title()} to be found: ')).lower()
            if to_be_found in file.read():
                for i, contact in enumerate(agenda):
                    if contact[find_by[options]] == to_be_found:
                        print(f'Contact nª{i+1} in the agenda')
                        print(f'\tName: {contact["name"]}'.title())
                        print(f'\tNote: {contact["note"]}')
                        print(f'\tE-mail: {contact["email"]}')
                        print(f'\tPhone: {contact["phone"]}')

                        contact['name'] = input('Type a new name: ')
                        contact['note'] = input('Type a new note: ')
                        contact['phone'] = input('Type a new phone number: ')

            else:
                print(f'{find_by[options].title()} not found')

    else:
        print('The agenda found zero contact registered')
        option = input('[1] - Add a new contact\n[2] - Verify if the file exist\n[3] - Back to menu\nOption: ')
        if option == '1':
            add_contact(agenda)
        if option == '2':
            pass
        if option == '3':
            main()
    new_phone = input('New phone: ')
    with open('data.txt') as file:
        list_of_lines = file.readlines()
    if new_phone == contact['phone']:
        list_of_lines[contact['phone']] = new_phone
        with open('data.txt', 'w') as file:
            for line in list_of_lines:
                file.write(line)
'''  # To be


def delete_contact(agenda):
    if len(agenda) > 0:
        print('===== DELETE CONTACT ====='.center(20))
        options = int(input('Find a contact by\n[1] Name\n[2] Age\n[3] Email\n[4] Phone\n>> '))
        find_by = {1: 'name',
                   2: 'note',
                   3: 'email',
                   4: 'phone'
                   }
        to_be_found = str(input(f'{find_by[options].title()} to be found: ')).lower()
        for i, contact in enumerate(agenda):
            if contact[find_by[options]] == to_be_found:
                print(f'Contact nª{i + 1} in the agenda')
                print(f'\tName: {contact["name"]}'.title())
                print(f'\tNote: {contact["note"]}')
                print(f'\tE-mail: {contact["email"]}')
                print(f'\tPhone: {contact["phone"]}')
    else:
        print('The agenda is empty')
    with open('data.txt', 'r') as file:
        lines = file.readlines()
    type_email = str(input(f"Type the contact's email for complete deletion: "))
    with open('data.txt', 'w') as file:
        for line in lines:
            if line.find(type_email) != -1:
                pass
            else:
                file.write(line)
    print('=' * 20)


def view_contact(agenda):
    if len(agenda) > 0:
        print('===== AGENDA ====='.center(20))
        for i, contact in enumerate(agenda):
            print(f'{i + 1}ª Contact')
            print(f'\tName: {contact["name"]}'.title())
            print(f'\tNote: {contact["note"]}')
            print(f'\tE-mail: {contact["email"]}')
            print(f'\tPhone: {contact["phone"]}')
        print('=' * 20)
        print(f'{len(agenda)} Contact(s) registered'.center(20))
    else:
        print('The agenda found zero contact registered')
        option = input('[1] - Add a new contact\n[2] - Verify if the file exist\n[3] - Back to menu\nOption: ')
        if option == '1':
            add_contact(agenda)
        if option == '2':
            pass
        if option == '3':
            main()


def main():
    agenda = load_contact()
    while True:
        option = input('\nWhat would you like to do?\n'
                       '[1] Add a new profile\n[2] Search a profile\n[3] Change an existing profile\n'
                       '[4] Delete an existing profile\n[5] View all profiles\n[6] Quit\nOption: ')
        if option == '1':
            add_contact(agenda)
            save_contact(agenda)
        elif option == '2':
            search_contact(agenda)
            '''
        elif option == '3': # To be finished
            change_contact(agenda)
            save_contact(agenda)
            '''
        elif option == '4':
            delete_contact(agenda)
        elif option == '5':
            view_contact(agenda)
        elif option == '6':
            print('Thank you for using our Agenda.')
            quit()
        else:
            print('\nPlease, type 1, 2, 3, 4, 5 or 6: ')
            continue


main()

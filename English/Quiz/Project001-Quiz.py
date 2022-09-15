# Projeto Quiz não finalizado.
from time import sleep
print("Welcome!")
play = str(input("Do you want to play? ")).upper()
if play == 'YES' or play == 'Y':
    print("Let's beginning")
    sleep(0.5)
    print('~'*70)
    print('There are 3 chances to get the answer right for each question.\n'
          'For each wrong answer for each question, 0.5 points are deducted.\n'
          '1st chance: +2.5\n2nd chance: +2.0\n3rd chance: +1.5.')
    print('~'*70)
    sleep(1)
else:
    print('Ok! Good bye...')
    quit()


def quiz(txt):
    perg = ["What does CPU stand for? ", "What does GPU stand for? ",
            "What does RAM stand for? ", "What does PSU stand for? "]
    respcer = ['central processing unit', 'graphics processing unit',
               'random access memory', 'power supply unit']
    c_total_wrong = c_question = c_wrong = 0
    pt = 0
    while c_question < 4:
        user = input(perg[c_question])
        if user != respcer[c_question].lower():
            c_wrong += 1
            c_total_wrong += 1
            print('Wrong answer.', end=' ')
            if c_total_wrong == 3:
                c_question += 1
                if c_question + 1:
                    c_total_wrong = 0
                    c_wrong = 0
                    print('\n')
        elif user == respcer[c_question].lower():
            c_total_wrong = 0
            c_question += 1
            if c_wrong == 0:
                pt += 2.5
            if c_wrong == 1:
                pt += 2.0
            if c_wrong == 2:
                pt += 1.5
            print('Congratulations!!')
            print()
            c_wrong = 0
            if c_question < 4:
                sleep(0.5)
                print('Next question.')
                sleep(0.5)
    print(f'You have completed the QUIZ and thanks for playing.\nYour final score: {pt}')


quiz('Your answer: ')

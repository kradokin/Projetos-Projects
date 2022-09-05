def readmon(txt):
    '''
    -> Replace str from "," to "."
    :param txt: read an input from test.py
    :return: return a float
    '''
    valid = False
    while not valid:
        enter = str(input(txt)).replace(',', '.').strip()
        if enter.isalpha() or enter == '':
            print(f'\033[0;31mError! \"{enter.upper()}\" is invalid.\033[m')
        else:
            valid = True
            return float(enter)

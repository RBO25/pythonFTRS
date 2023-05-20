import random


def passgen():
    count = int(input("How many: "))
    password = ''

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '1234567890'
    signs = '!@#$%^&'
    sumlist = ''
    sumlist += alphabet
    choise = input('Use digits (y/n)? ')
    if choise == 'y' or choise == 'yes':
        sumlist += digits
    choise = input('Use UPPERCASE (y/n)? ')
    if choise == 'y' or choise == 'yes':
        sumlist += alphabet2
    choise = input('Use signs (y/n)?')
    if choise == 'y' or choise == 'yes':
        sumlist += signs
    for i in range(1, count +1):
        password += random.choice(sumlist)
    print(password)

passgen()
#!/bin/usr/env python3

s_list = list()


def shopping_list():
    name = input('Enter item: ')
    s_list.append(name)
    amount = int(input('Enter amount: '))
    s_list.append(amount)


print('Welcome to the shopping list?')
print('Press Q to exit.')
while input('Add items? ') != 'Q':
    shopping_list()
print(s_list, sep=' ')

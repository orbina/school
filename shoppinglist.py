#!/bin/usr/env python3

s_list = list()


def shopping_list():
    name = input('Enter item: ')
    s_list.append(name) # Add item to list
    amount = int(input('Enter amount: '))
    s_list.append(amount) # Add amount to list


print('Welcome to the shopping list?')
print('Press "n" to exit.')
while input('Add items? Y/n ') != 'n': # Loop the list
    shopping_list()
print(s_list, sep=' ') # Print finished list

#!/bin/usr/env python3

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def month():
    choice = input('> ')
    if choice == '1': # Print all months
        print(months, sep=' ')
    elif choice == '2': # Print months sorted in alphabetical order
        print(sorted(months))
    elif choice == '3': # Print only first letter of each month
        for letter in months:
            print(letter[0]) 
    else:
        print('Sorry, non capisco un cazzo.')


print('Choose')
print('1. Months in the year')
print('2. Months sorted alphabetically')
print('3. Months by first letter')
print('Enter your choice:')
month()

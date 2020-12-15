#!/usr/bin/env python3
import os

welcome = ('Welcome ' + os.getlogin())
what = 'Would you like to print a car or a house?'

print(welcome)
print(what)
a = input('Car/House:')
if a.lower() == 'house':
    print("      ':.")
    print("         []_____")
    print('        /\      \ ')
    print('    ___/  \__/\__\__')
    print("---/\___\ |''''''|__\-- ---")
    print("   ||'''| |''||''|''|")
    print('   ``"""`"`""))""`""`')
elif a.lower() == 'car':
    print('  ______')
    print(' /|_||_\`.__')
    print("(   _    _ _\ ")
    print("=`-(_)--(_)-'")
else: print ('Sorry, I did not understand that, try again.')

#!/usr/bin/env python3

print('Calculate volume of a rectangular tank.')
le = input('Enter length of tank (cm): ')
wi = input('Enter width of tank (cm): ')
he = input('Enter height of tank (cm): ')
volume = le*int(wi)*int(he)
if volume != 0:
    print('Volume (in cm2) of the tank is: ' + str(volume) + ' cm2.')
elif volume == 0:
    print('Error. One of the inputs were 0, please try again.')

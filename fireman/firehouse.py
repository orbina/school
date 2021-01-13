#!/bin/usr/env python3

from fireman import *

# Create a Fireman object
fireman_one = fireman()
fireman_one.name = 'John'
fireman_one.surname = 'Doe'
fireman_one.age = '24'
fireman_two = fireman()
fireman_two.name = 'Bruno'
fireman_two.surname = 'Hanson'
fireman_two.age = '29'
fireman_three = fireman()
fireman_three.name = 'James'
fireman_three.surname = 'Brimi'
fireman_three.age = '54'

print('Number {}: {} {}, age {}'.format(fireman_one.number, fireman_one.name, fireman_one.surname, fireman_one.age))
print('Number {}: {} {}, age {}'.format(fireman_two.number, fireman_two.name, fireman_two.surname, fireman_two.age))
print('Number {}: {} {}, age {}'.format(fireman_three.number, fireman_three.name, fireman_three.surname, fireman_three.age))
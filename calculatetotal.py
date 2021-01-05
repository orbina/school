#!/usr/bin/env python3

total = 0
add = int(input('Enter a value: '))

while add != -1:
    total += add
    add = int(input('Enter value: '))

print('Total value: ', total)

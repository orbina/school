#!/usr/bin/env python3

def similar(food1, food2):
    return list(list(set(food1)-set(food2)) + list(set(food2)-set(food1)))


food1 = ['Pizza', 'Hamburger', 'Kebab', 'Panini', 'Sushi']
food2 = ['Pizza', 'Arrosticini', 'Kebab', 'Sushi', 'Baguette']

print('Similar food:')
print(*similar(food1, food2))

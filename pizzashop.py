#!/usr/bin/env python3

base = input('Thick/Thin: ')
if base.lower() == 'thick':
    baseprice = 10
elif base.lower() == 'thin':
    baseprice = 5
else:
    exit('Input unknown.')

size = input('Small/Medium/Large: ')
if size.lower() == 'small' or size.lower() == 's':
    sizeprice = 30
elif size.lower() == 'medium' or size.lower() == 'm':
    sizeprice = 40
elif size.lower() == 'large' or size.lower() == 'l':
    sizeprice = 50
else:
    exit('Input unknown.')

sauce = input('Tomato/Barbecue: ')
if sauce.lower() == 'tomato':
    sauceprice = 5
elif sauce.lower() == 'barbecue' or sauce.lower() == 'bbq':
    sauceprice = 10
else:
    exit('Input unknown.')

topping1 = input('Cheese (Y/n): ')
if topping1.lower() == 'yes' or topping1.lower() == 'y':
    cheese = 5
elif topping1.lower() == 'no' or topping1.lower() == 'n':
    cheese = 0
else:
    exit('Input unknown.')

topping2 = input('Mushrooms (Y/n): ')
if topping2.lower() == 'yes' or topping2.lower() == 'y':
    mushrooms = 3
elif topping2.lower() == 'no' or topping2.lower() == 'n':
    mushrooms = 0
else:
    exit('Input unknown.')

topping3 = input('Avocado (Y/n): ')
if topping3.lower() == 'yes' or topping3.lower() == 'y':
    avocado = 7
elif topping3.lower() == 'no' or topping3.lower() == 'n':
    avocado = 0
else:
    exit('Input unknown.')

topping4 = input('Pineapple (Y/n): ')
if topping4.lower() == 'yes' or topping4.lower() == 'y':
    pineapple = 0
    print("No pineapple on pizza! Get out of my store!")
    exit(0)
elif topping4.lower() == 'no' or topping4.lower() == 'n':
    pineapple = 0
    print('Good boy!')
else:
    exit('Input unknown.')

topping5 = input('Bacon (Y/n): ')
if topping5.lower() == 'yes' or topping5.lower() == 'y':
    bacon = 7
elif topping5.lower() == 'no' or topping5.lower() == 'n':
    bacon = 0
else:
    exit('Input unknown.')

topping6 = input('Chicken (Y/n): ')
if topping6.lower() == 'yes' or topping6.lower() == 'y':
    chicken = 7
elif topping6.lower() == 'no' or topping6.lower() == 'n':
    chicken = 0
else:
    exit('Input unknown.')

topping7 = input('Fish (Y/n): ')
if topping7.lower() == 'yes' or topping7.lower() == 'y':
    fish = 6
elif topping7.lower() == 'no' or topping7.lower() == 'n':
    fish = 0
else:
    exit('Input unknown.')

print('Total price:')
print(baseprice + sizeprice + sauceprice + cheese + mushrooms + avocado + pineapple + bacon + chicken + fish)

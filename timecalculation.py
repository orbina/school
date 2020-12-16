#!/usr/bin/env python3


min = int(input('Enter whole minutes worked current month: '))

hour = int(min/60)
min2 = int(min%60)
days = int(hour/8)
hours = int(hour%8)
if days and hours and min2 != 0:
    print('You have worked ' + str(days) + ' days, ' + str(hours) + ' hours, and ' + str(min2) + ' minutes.')
else:
    exit("You haven't worked")

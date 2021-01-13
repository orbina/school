#!/bin/usr/env python3

class fireman:
    count = 0

    def __init__(self):
        self.name = ''  # Assign to an instance variable (instance variables created by assigning variable to the self object)
        self.surname = ''  # Assign to an instance variable
        fireman.count += 1  # Assign to the class variable <- class attribute, so all firemen created will share same value
        self.number = fireman.count  # Assign to an instance variable
        self.age = ''
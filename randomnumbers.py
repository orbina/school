#!/bin/usr/env python3
import random

print('Enter name of file to write to.')
user_file_name = input('> ')  # User created filename
file_name = user_file_name + '.txt'  # Appending .txt to the filename
write_to_file = open(file_name, 'w')  # Opening the newly added file

for i in range(1, 101):  # Creating a loop for generating the random numbers
    line = str(random.randint(0, 501))
    write_to_file.write(line + '\n')  # Writing the random numbers to the named file

write_to_file.close()

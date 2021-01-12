#/bin/usr/env python3

try:  # Checks if file exists before opening
    csv_file = open('mycsv.csv')
    file_contents = csv_file.readlines()
    # The individual lines are stored as elements in a string-based list
    # Using a for-loop allows to print line by line, instead of all on one line
    for line in file_contents:
        print(line, end='')
except IOError:  # If file does not exist, abort program.
    print('File does not exist, aborting')
finally:  # Close the file when the
    csv_file.close()
    

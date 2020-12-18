#!/usr/bin/env python3

phonebook = {
    'Pizza': '22 22 55 55',
    'Kykkelikokkos': '815 493 00',
    'DnB': '04800',
    'FirmaAS': '23 45 67 89',
    'Nok-et-firma': '987 65 432'
}

entry = input('Would you like to add a new entry? Y/n: ')
if entry.lower() == 'yes' or entry.lower() == 'y':
    newname = input('Enter the company name: ')
    if newname == '':
        exit('Error, no input. Exiting.')
    newnumber = input('Enter the company number: ')
    if newnumber == '':
        exit('Error, no input. Exiting.')
    phonebook[newname] = newnumber

print('Would you like to search the phonebook?')
search = input('Yes/no/Show All. ')
if search.lower() == 'yes' or search.lower() == 'y':
    searching = input('Enter a company name: ')
    if searching in phonebook.keys():
        print(phonebook[searching])
    else:
        print('Company name not found.')
elif search.lower() == 'show all' or search.lower() == 'all' or search.lower() == 'show' or search.lower() == 's':
    print(phonebook)
elif search.lower() == 'no' or search.lower() == 'n':
    exit('Not searching.')
else:
    exit('I did not understand that. Start over.')

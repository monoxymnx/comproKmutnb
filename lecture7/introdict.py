phonebook = {'Watchakorn': '123-4567', 'John': '987-6543', 'Alice': '555-1234'}
print(phonebook)

print(phonebook['John'])
print(phonebook.get('Alice'))

key = 'Pluto'
if key in phonebook:
    print(phonebook['pluto'])
else:
    print(key + ' not in phonebook')

phonebook['Simson'] = '111-2222'
phonebook['pluto'] = '333-4444'
phonebook['John'] = '999-8888'
print(phonebook)

del phonebook['Simson']
print(phonebook)
for i in range(5):
    print(i)
print('-----------------------------------------------------------')

for i in range(3,10):
    print(i)
print('-----------------------------------------------------------')

for i in range(1,11,2):
    print(i)
print('-----------------------------------------------------------')

print('Number\tSquare')
print('-------------------')

inputSquare = int(input('enter square '))
for number in range(1,11):
    multiple = number * inputSquare
    print(number, '\t', multiple)
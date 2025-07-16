number = [6,5,3,8,4,2,5,4,11]
sum = 0
for val in number:
    sum += val
    print(sum)
print(f'The sum of the numbers is {sum}')


print('-----------------------------------------------------------')
max = 5
total = 0
print('This program calculates the sum of')
print(max, 'number you will enter.')
for counter in range(max):
    number = int(input('Enter a number: '))
    total += number
print('The total is', total )

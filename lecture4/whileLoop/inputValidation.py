score = int(input('Enter a test score: '))
while score < 0 or score > 100:
    print('Error: The score cannot be negative')
    score = int(input('Enter a test correct score: '))
print(f'The score is {score}')
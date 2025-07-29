def is_armstrong(numbers):
    
    number = str(numbers)
    length = len(number)
    InitializeTotal = 0
    
    for digit in number:
        InitializeTotal += int(digit) ** length
    return InitializeTotal == numbers

print(is_armstrong(153))  
print(is_armstrong(9474))  
print(is_armstrong(123))  
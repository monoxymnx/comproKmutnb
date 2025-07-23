def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))

def findMax (*args):
    if not args:
        return None
    maxValue = args[0]
    for number in args:
        if number > maxValue:
            maxValue = number
    return maxValue

result = findMax(3,5,7,2,8)
print(f"The maximum value is: {result}")

def printAll(*args):
    for index , arg in enumerate(args):
        print(f"Argument {index + 1}: {arg}")
printAll("Python",3.8,True,[1,2,3,],{"key": "value"})
def calculateStats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum

numbers = [5,10,15,20,25]
total, avg, maxNum, minNum = calculateStats(numbers)
print(f"Total: {total}, Average: {avg}, Maximum: {maxNum}, Minimum: {minNum}")

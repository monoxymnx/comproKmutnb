try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print("Result is:", result)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

print("End of program")
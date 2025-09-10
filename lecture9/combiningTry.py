try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by 0 is not allowed.")
else:
    print("Result is:", result)
finally:
    print("Execution completed.")

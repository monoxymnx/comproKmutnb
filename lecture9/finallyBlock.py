try:
    numberator = float(input("Enter a numberator: "))
    denominator = float(input("Enter a denominator: "))
    result = numberator / denominator
    print("Result is:", result)
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
finally:
    print("Execution completed.")
print("End of program")
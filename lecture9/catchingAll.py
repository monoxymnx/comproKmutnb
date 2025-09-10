try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print("Result is:", result)
except Exception as e:
    print("An error occurred:", e)
print("End of program")

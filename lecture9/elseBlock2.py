def divide(a,b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Exception:", e)
    else:
        print("Result is:", result)

a,b = map(int, input().split())
print(divide(a,b))
print("End of program")
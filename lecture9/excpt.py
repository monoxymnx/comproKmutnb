# x = 1/0
# print("This will not be printed due to the exception above.")

try:
    x=1/2
    print(f"x = {x}")
except ZeroDivisionError as e:
    print("Caught a division by zero error:", e)

print("end of program")
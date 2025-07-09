num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (1 +, 2 -, 3 *, 4 /): ")

if operation == "1":
    result = num1 + num2
elif operation == "2":
    result = num1 - num2
elif operation == "3":
    result = num1 * num2
elif operation == "4":
    result = num1 / num2
else:
    result = "ผลลลัพธ์ไม่ถูกต้อง"

print("ผลลัพธ์:", result)
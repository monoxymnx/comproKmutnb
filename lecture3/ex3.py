worked = int(input("Enter the number of hours worked: "))
pay_rate = int(input("Enter the pay rate: "))
if worked > 40:
    overtime = (worked - 40) * (pay_rate * 1.5) + 40 * pay_rate
else:
    overtime = worked * pay_rate
print("Overtime pay: $", overtime)
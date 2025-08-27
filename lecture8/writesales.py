num_day = int(input("Enter number of days: "))
with open('sales.txt', 'w') as sales_file:
    for count in range (1 , num_day + 1):
        sales = float(input(f"Enter sales for day {count}: "))
        sales_file.write(f"{sales}\n")
print('data written to sales.txt')
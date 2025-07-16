keep_going = 'y'
while keep_going.lower() == 'y':
    sales = float(input("Enter sales amount: "))
    comm_rate = float(input("enter the commission rate: "))
    commission = sales * comm_rate
    print(f'The commission is ${commission:.2f}')
    keep_going = input("do you want to calculate another commission (Enter y for yes , n for no): ")
else:
    print("end calculated")
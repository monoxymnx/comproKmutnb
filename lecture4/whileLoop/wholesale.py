keep_going = 'y'
while keep_going.lower() == 'y':
    cost = float(input('enter the item cost: '))
    retail_price = cost*2.5
    print(f'The retail price is ${retail_price:.2f}')
    keep_going = input("do you want to calculate another retail price (Enter y for yes , n for no): ")
    if keep_going.lower() == 'n':
        break
    while keep_going.lower() != 'y':
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        keep_going = input("Please enter 'y' for yes or 'n' for no: ")
        if keep_going.lower() == 'n':
            break
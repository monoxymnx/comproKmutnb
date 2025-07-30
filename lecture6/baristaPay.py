num_employees = 6
def main():
    hours = [0] * num_employees
    for index in range(num_employees):
        print('enter the hours worked by employee',
              index + 1, ':', sep='', end=' ')
        hours[index] = float(input())

    payrate = float(input("enter the hourly pay rate: "))
    for index in range(num_employees):
        gross_pay = hours[index] * payrate
        print('Gross pay for employee', index + 1, ': $',
              format(gross_pay, '.2f'), sep='')

main()
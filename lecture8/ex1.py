with open('employees.txt', 'r') as emp_file:
    for line in emp_file:
        print(line.strip())

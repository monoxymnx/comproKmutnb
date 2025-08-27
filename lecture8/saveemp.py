num_emps = int(input("how many employee records do you want to create?"))
with open('employees.txt' , 'w') as emp_file:
    for count in range(1,num_emps + 1):
        name = input("name: ")
        id_num = input("ID number: ")
        dept = input("department: ")
        emp_file.write(f"name: {name}\nID number: {id_num}\ndepartment: {dept}\n")
        print()

print('Employee records written to employees.txt')

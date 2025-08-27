import struct
num_record = int(input('How many records do you want to create? '))
with open('records.bin',"wb") as file:
    for _ in range(num_record):
        id_num = int(input("Enter ID: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gpa = float(input("Enter GPA: "))
        data = struct.pack('i20sif', id_num, name.encode(), age, gpa)
        file.write(data)
print(f"{num_record} records written to records.bin")
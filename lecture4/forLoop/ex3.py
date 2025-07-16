row = int(input("Enter the number of rows: "))
numberRow = 100//row
for i in range(row):
    start = i * numberRow + 1
    end = start + numberRow - 1
    for j in range(start, end + 1):
        print(j, end=' ')
    print()
filename = input("Enter filename: ")
try:
    infile = open(filename, 'r')
    contents = infile.read()
    print(contents)
    infile.close()
except IOError:
    print("An error occurred trying to read the file:", filename)

print('end of program')
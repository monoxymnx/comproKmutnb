inchar = input("Input a character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("You input an uppercase character", inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("You input a lowercase character")
elif inchar >= '0' and inchar <= '9':
    print("You input a Number",inchar)
else:
    print("it's anot a letter or a number",inchar)
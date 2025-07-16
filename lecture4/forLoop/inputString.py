input_string = input("enter string: ")
vowels = "AEIOU"
modified_str = ""

for char in input_string:
    if char.upper() in vowels:
        modified_str += "x"
    else: modified_str += char

print("Modified str: ", modified_str)
def isArmstrong(number):
    digits = str(number)
    num_digits = len(digits)
    terms = []
    total = 0
    for digit in digits:
        val = int(digit) ** num_digits
        terms.append(f"{digit}**{num_digits}")
        total += val

    expression = " + ".join(terms)
    result = total == number
    print(f"Output: {result}  ({expression} = {total})")
    return result

# Example usage
isArmstrong(153) 
isArmstrong(9474)
isArmstrong(123)

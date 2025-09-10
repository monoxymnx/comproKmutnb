class NegativeValueError(Exception):
    def __int__(self, value):
        self.value = value
        super().__init__(f"Negative value error: {value} is not allowed.")
def check_position_number(num):
    if num<0:
        raise NegativeValueError(num)
    else:
        print(f"{num} is a valid position number.")
try:
    number = int(input("Enter a position number: "))
    check_position_number(number)
except NegativeValueError as e:
    print(e)
except ValueError:
    print("Invalid input! Please enter an integer.")
finally:
    print("Execution completed.")
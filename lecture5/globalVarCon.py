import random
HEADES = 1
TAILS = 2
TOSSES = int(input("Enter the number of coin tosses: "))
def tossesCoin():
    for toss in range(TOSSES):
        if random.randint(HEADES, TAILS) == HEADES:
            print("Heads")
        else:
            print("Tails")
tossesCoin()
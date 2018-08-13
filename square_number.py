import math
def is_square(n):
    try:
        int(n)
        if int(n) > 0 and math.sqrt(int(n)) % 1 == 0:
            return n + " is a square number."
        else:
            return n + " is not a square number."
    except ValueError:
        return n +" is not an integer number. Next time, enter an integer number."

n = input("Please, enter an integer number: ")
print(is_square(n))


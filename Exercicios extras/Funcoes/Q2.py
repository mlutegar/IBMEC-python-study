# QUESTION 2
# Read a set of 30 numbers
# Creat a function of 1 argument, return P if positive and N if negative or zero

def signal(a):
    if a > 0:
        return "P"
    else:
        return "N"


for i in range(30):
    n = float(input("\nInput a number: "))
    print("The informed number is", signal(n))

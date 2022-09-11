# QUESTION 6
# Read an integer number
# Use a function that make this:
#                               1
#                               1 2
#                               1 2 3
#                               ...
#                               1 2 ... n

def pyramid(n):
    for column in range(n):
        print('')
        for row in range(column + 1):
            print(row + 1, " ", end="")


number = int(input("Input a integer number: "))
pyramid(number)

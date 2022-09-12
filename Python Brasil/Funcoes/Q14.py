# QUESTION 14
# Create a magic square, 3 rows and 3 columns
# Where the sum of numbers 3 in a row, columns and diagonal is the same
# Ex:
# 8  3  4
# 1  5  9
# 6  7  2
#
# Creat a function that make all possible magic square
# Tip: Produce all possible combinations and check the sum when completing each square.
# Using a vector from 1 to 9 seems to be simpler than using a 3x3 matrix.

def square():
    for column in range(3):
        print("")
        for row in range(3):
            print("x ", end="")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

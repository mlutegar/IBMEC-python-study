# QUESTION 5
# Read an integer number
# Creat a function that make this:
#                                  1
#                                  2 2
#                                  3 3 3
#                                  ...
#                                  n n n n n n n ... n

def pyramid(n):
    for i in range(n):
        text = str(i+1) + ' '
        print(text * (i+1))


number = int(input("Input a integer number: "))
pyramid(number)

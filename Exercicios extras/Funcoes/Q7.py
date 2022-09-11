# QUESTION 7
# Read 2 integers numbers
# Creat a function:
# That determiner how many dividers the first number have
# And how much are bigger that the second number

def dividers_bigger(a, b):
    qtd = 0
    for i in range(a):
        if a % (i+1) == 0:
            if a // (i+1) > b:
                qtd += 1
    return qtd


a = int(input("Input the first number: "))
b = int(input("Input the second number: "))

print("\nExist", dividers_bigger(a, b), "dividers of", a, "that are bigger than", b)

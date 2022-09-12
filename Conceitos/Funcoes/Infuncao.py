def op(x, y):
    if par(x) == 0:
        return x * y ** 2
    else:
        return x * y


def par(n):
    if n % 2 == 0:
        return 0
    else:
        return 1


a = float(input("Input the first number: "))
b = float(input("Input the second number: "))

if par(a) == 0:
    print("\nThe first number is pair")
else:
    print("\nThe first number is odd")

print("The result then is", op(a, b))

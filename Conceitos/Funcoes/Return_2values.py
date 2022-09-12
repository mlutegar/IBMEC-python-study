def op(x, y):
    return x * y ** 2, x * y


a = int(input('Input A: '))
b = int(input('Input B: '))
x = op(a, b)
print(x)

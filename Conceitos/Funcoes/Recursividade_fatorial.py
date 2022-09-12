def factorial(x):
    result = 1
    for i in range(x):
        result = factorial(x-1) * x
    return result


print(factorial(5))

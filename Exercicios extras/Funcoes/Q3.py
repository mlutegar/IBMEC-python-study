# QUESTION 3
# Read an integer number
# Creat a function, of 1 argument, that invert a digit sequence


def inverted(number):
    text = ""
    while (number // 10) != 0:
        text += str(number % 10)
        number = (number // 10)
        if number//10 == 0:
            text += str(number)
    return text


n = int(input("Input an integer number: "))
print("The number inverted is", inverted(n))

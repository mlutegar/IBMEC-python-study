# QUESTION 1
# Read 30 sets of 3 numbers;
# Creat a function that read 3 arguments and creat a set
# Pick the smaller number of each set and calculate the media in the end

def minimum(a, b, c):
    return min(a, b, c)


qtd = 0
total = 0

for i in range(3):
    print("\nAbout the", i + 1, "set")
    total += minimum(float(input("Input a: ")), float(input("Input b: ")), float(input("Input c: ")))
    qtd += 1

print(
    "\nThe quantity of numbers was: ", qtd,
    "\nThe media was: ", total / qtd
)

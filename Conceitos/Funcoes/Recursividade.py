def sums_pa(initial_term, ratio, quantity):
    sums = 0
    for i in range(quantity):
        sums = sums_pa(initial_term + ratio, ratio, quantity - 1) + initial_term
    return sums


a1 = int(input("Input the initial term: "))
r = int(input("Input the ratio term: "))
n = int(input("Input the quantity of P.A.: "))

print("\nThe P.A. sum is:", sums_pa(a1, r, n))

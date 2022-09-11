# QUESTION 4
# Input amount to pay in restaurant
# Create a function that calculate the tip of waiter
# Tip is 10% of amount to pay
# Show the price without the tip and the tip

def tip(n):
    return n * 0.10


bill = int(input("Inform the final amount of the bill if paying at the restaurant: "))

print(
    "\nThe bill was: $", bill - tip(bill),
    "\nThe tip of waiter was: $", tip(bill),
)

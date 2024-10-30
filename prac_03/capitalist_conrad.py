"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

# Constants for price simulation
MAX_INCREASE = 0.175  # 17.5% increase
MAX_DECREASE = 0.05  # 5% decrease
MIN_PRICE = 1.00  # Minimum price of $1
MAX_PRICE = 100.00  # Maximum price of $100
INITIAL_PRICE = 10.0  # Starting price
FILENAME = "stock_prices.txt"  # File to write output

# Initialize the price and day counter
price = INITIAL_PRICE
day = 0

# Open the file for writing
out_file = open(FILENAME, 'w')

# Write the starting price to the file
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulation loop
while MIN_PRICE <= price <= MAX_PRICE:
    day += 1  # Increment the day counter
    price_change = 0

    # Generate a random integer of 1 or 2
    # If it's 1, the price increases; otherwise, it decreases
    if random.randint(1, 2) == 1:
        # Generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    # Update the price based on the change
    price *= (1 + price_change)

    # Write the price at the end of the day to the file
    print(f"On day {day} price is: ${price:,.2f}", file=out_file)

# Final price output after the loop ends
print(f"Final price after {day} days: ${price:,.2f}", file=out_file)

# Close the file
out_file.close()

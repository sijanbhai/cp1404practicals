import random

# Starting price
price = 10.00

# Simulate until the price goes out of bounds
while 0.01 <= price <= 1000:
    # Determine if the price goes up or down
    if random.randint(0, 1) == 0:
        # Price decreases by 0 to 5%
        price_change = random.uniform(0, 0.05)
        price -= price * price_change
    else:
        # Price increases by 0 to 10%
        price_change = random.uniform(0, 0.10)
        price += price * price_change

    # Print the price, rounded to 2 decimal places
    print(f"Stock price: ${price:.2f}")

print("Simulation ended.")

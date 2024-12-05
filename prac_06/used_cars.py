"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)
    # Create a new Car object called "limo" with 100 units of fuel
    limo = Car(100)
    print(f"Limo has fuel: {limo.fuel}")
    print(limo)
    # Add 20 more units of fuel to the limo
    limo.add_fuel(20)
    print(f"After refueling, limo has fuel: {limo.fuel}")
    # Print the amount of fuel in the limo
    print(f"Final amount of fuel in limo: {limo.fuel}")
    # Attempt to drive the limo 115 km
    distance_driven = limo.drive(115)
    print(f"Limo drove {distance_driven} km.")
    print(f"Remaining fuel in limo: {limo.fuel}")
    # Verify the __str__ method directly with str()
    print(f"String representation of 'my_car': {str(my_car)}")  # Output: My Car, fuel=150, odometer=30
    print(f"String representation of 'limo': {str(limo)}")  # Output: Limo, fuel=5, odometer=115


main()
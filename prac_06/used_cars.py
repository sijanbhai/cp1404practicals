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


main()
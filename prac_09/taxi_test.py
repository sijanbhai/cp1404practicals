# Import the Taxi class from the taxi module
from taxi import Taxi

# Create a Taxi object with name "Prius 1" and fuel level 100
my_taxi = Taxi("Prius 1", 100)

# Print the taxi's details
print(my_taxi)

# Drive the taxi for 40 km
my_taxi.drive(40)
print(f"Fare: ${my_taxi.get_fare():.2f}")

# Start a new fare and drive for 100 km
my_taxi.start_fare()
my_taxi.drive(100)
print(f"Fare: ${my_taxi.get_fare():.2f}")

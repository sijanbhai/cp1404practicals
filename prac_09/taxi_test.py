# Import the Taxi class from the taxi module
from taxi import Taxi

# Create a new Taxi object with the specified attributes
my_taxi = Taxi("Prius 1", 100, 1.23)

# Display the string representation of the taxi object
print(my_taxi)

# Start a new fare
my_taxi.start_fare()

# Drive the taxi for 50 kilometers
my_taxi.drive(50)

# Print the taxi's details and the current fare
print(f"Taxi details after driving 50 km: {my_taxi}")
print(f"Current fare after driving 50 km: ${my_taxi.get_fare():.2f}")

# Drive the taxi for an additional 40 kilometers
my_taxi.drive(40)

# Print the taxi's details and the current fare after driving 40 more km
print(f"Taxi details after driving an additional 40 km: {my_taxi}")
print(f"Current fare after driving 90 km: ${my_taxi.get_fare():.2f}")

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

# Display the taxi's information after driving 50 km
print(my_taxi)

# Print the fare for the first 50 km trip
print(f"Fare for the first 50 km trip: ${my_taxi.get_fare():.2f}")

# Drive the taxi for an additional 40 kilometers
my_taxi.drive(40)

# Display the taxi's information after driving 40 more km
print(my_taxi)

# Print the fare for the entire trip (50 km + 40 km)
print(f"Fare for the entire trip: ${my_taxi.get_fare():.2f}")

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

# Display the taxi's information after driving
print(my_taxi)

# Print the fare for the current trip
print(f"Fare for the trip: ${my_taxi.get_fare():.2f}")

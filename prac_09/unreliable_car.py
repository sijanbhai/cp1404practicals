import random
from car import Car


class UnreliableCar(Car):
    """ A Car that sometimes won't drive due to its reliability. """

    def __init__(self, name, fuel, reliability):
        """ Initialize an UnreliableCar instance. """
        super().__init__(name, fuel)  # Call the parent class's __init__ method
        self.reliability = reliability  # Reliability is a float between 0 and 100

    def drive(self, distance):
        """ Drive the car, but sometimes fail due to reliability. """
        # Generate a random number between 0 and 100
        random_number = random.randint(0, 100)

        # If the random number is less than reliability, drive the distance
        if random_number < self.reliability:
            return super().drive(distance)  # Call the parent class's drive method
        else:
            return 0  # If reliability fails, don't drive any distance

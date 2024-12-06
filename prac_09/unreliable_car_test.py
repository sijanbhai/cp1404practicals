import random
from unreliable_car import UnreliableCar


def test_unreliable_car():
    reliability = 30  # 30% chance of driving
    car = UnreliableCar("Unreliable", 100, reliability)

    successful_drives = 0
    total_drives = 100

    for _ in range(total_drives):
        distance_driven = car.drive(10)  # Attempt to drive 10 km
        if distance_driven > 0:
            successful_drives += 1

    # The successful drives should roughly be 30% of total attempts
    print(f"Attempted to drive {total_drives} times.")
    print(f"Successfully drove {successful_drives} times.")
    print(f"Success rate: {successful_drives / total_drives * 100}%")

    # Check if the result is close to the expected success rate
    assert (reliability - 10) <= (successful_drives / total_drives * 100) <= (reliability + 10), \
        "Reliability test failed!"


# Run the test
test_unreliable_car()

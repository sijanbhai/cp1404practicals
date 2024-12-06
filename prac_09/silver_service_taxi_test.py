from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    """Test the SilverServiceTaxi class."""
    # Create a SilverServiceTaxi object
    taxi = SilverServiceTaxi("Hummer", 200, fanciness=2)

    # Drive the taxi 18 km
    taxi.start_fare()
    taxi.drive(18)

    # Check fare calculation
    fare = taxi.get_fare()
    print(taxi)  # Should include fuel, odometer, fare distance, price/km, and flagfall
    print(f"Fare: ${fare:.2f}")

    # Assert the fare is calculated correctly
    expected_fare = 18 * taxi.price_per_km + SilverServiceTaxi.flagfall
    assert abs(fare - expected_fare) < 0.01, f"Expected ${expected_fare:.2f}, but got ${fare:.2f}"

# Run the test
test_silver_service_taxi()

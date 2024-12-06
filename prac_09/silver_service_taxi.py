from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with additional features for luxury service."""

    flagfall = 4.50  # Class variable for flagfall charge

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)  # Call Taxi's __init__
        self.price_per_km *= fanciness  # Scale price_per_km by fanciness

    def get_fare(self):
        """Calculate the total fare."""
        # Add the flagfall to the base fare
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

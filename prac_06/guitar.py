class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate the age of the guitar."""
        current_year = 2024  # Adjust this as needed
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50 years or older)."""
        return self.get_age() >= 50

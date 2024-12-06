class Band:
    """Band class to represent a band of musicians."""

    def __init__(self, name=""):
        """Initialize the Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band and its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string of all musicians playing their instruments."""
        return "\n".join(musician.play() for musician in self.musicians)

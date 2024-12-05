from guitar import Guitar

def main():
    """Program to manage a collection of guitars."""
    guitars = []

    print("My guitars!")
    while True:
        name = input("Name: ")
        if not name:  # Stop input when a blank name is entered
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")

# Uncomment the following lines for testing without input
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
# guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))

if __name__ == "__main__":
    main()

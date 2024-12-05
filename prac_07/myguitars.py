import csv
from guitar import Guitar


def main():
    """Read, display, add new guitars, and write them back to a CSV file."""
    filename = "guitars.csv"
    guitars = read_guitars_from_file(filename)

    # Display the current list of guitars
    print("\nCurrent guitars:")
    for guitar in guitars:
        vintage_status = " (vintage)" if guitar.is_vintage() else ""
        print(f"{guitar}{vintage_status}")

    # Allow the user to add new guitars
    print("\nAdd new guitars:")
    add_new_guitars(guitars)

    # Sort the list by year
    guitars.sort()

    # Display all guitars sorted by year
    print("\nThese are all the guitars (sorted by year):")
    for guitar in guitars:
        vintage_status = " (vintage)" if guitar.is_vintage() else ""
        print(f"{guitar}{vintage_status}")

    # Write the updated list back to the file
    write_guitars_to_file(filename, guitars)
    print(f"\nAll guitars have been written back to {filename}.")


def read_guitars_from_file(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for line in reader:
            name, year, cost = line[0], int(line[1]), float(line[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def add_new_guitars(guitars):
    """Prompt the user to enter new guitars and add them to the list."""
    while True:
        name = input("Enter guitar name (or press Enter to finish): ")
        if not name:
            break
        try:
            year = int(input("Enter the year of manufacture: "))
            cost = float(input("Enter the cost of the guitar: "))
            guitars.append(Guitar(name, year, cost))
            print(f"{name} ({year}) : ${cost:,.2f} added.")
        except ValueError:
            print("Invalid input. Please enter valid numbers for year and cost.")


def write_guitars_to_file(filename, guitars):
    """Write the list of guitars back to the CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()

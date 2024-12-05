import csv
from guitar import Guitar


def main():
    """Read guitar data from a CSV file, sort by year, and display details."""
    filename = "guitars.csv"
    guitars = read_guitars_from_file(filename)

    # Sort the list of guitars by year (oldest to newest)
    guitars.sort()

    print("\nThese are the guitars (sorted by year):")
    for guitar in guitars:
        vintage_status = " (vintage)" if guitar.is_vintage() else ""
        print(f"{guitar}{vintage_status}")


def read_guitars_from_file(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for line in reader:
            name, year, cost = line[0], int(line[1]), float(line[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


if __name__ == "__main__":
    main()

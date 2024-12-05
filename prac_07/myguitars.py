import csv
from guitar import Guitar


def main():
    """Read guitar data from a CSV file and display the details."""
    filename = "guitars.csv"
    guitars = read_guitars_from_file(filename)

    print("\nThese are the guitars:")
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

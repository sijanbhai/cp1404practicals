"""
Wimbledon Champions Analysis

Estimate Time: 45 minutes
Actual Time: 40 minutes
"""
import csv

def read_file(filename):
    """
    Reads the data from the given CSV file and returns it as a list of lists.
    The file is read with UTF-8-sig encoding to handle the BOM.
    """
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header
        for row in reader:
            data.append(row)
    return data

def get_champions_and_counts(data):
    """
    Processes the data to count the number of wins for each champion.

    Args:
    data (list of lists): The input data from the CSV file.

    Returns:
    dict: A dictionary where the keys are champion names and the values are win counts.
    """
    champion_counts = {}
    for row in data:
        champion = row[2]
        champion_counts[champion] = champion_counts.get(champion, 0) + 1
    return champion_counts

def get_champion_countries(data):
    """
    Extracts the set of countries of champions.

    Args:
    data (list of lists): The input data from the CSV file.

    Returns:
    set: A set of unique champion countries.
    """
    champion_countries = {row[1] for row in data}
    return champion_countries

def main():
    filename = "wimbledon.csv"  # Replace with your file name
    data = read_file(filename)

    # Get champions and their win counts
    champions = get_champions_and_counts(data)

    # Get countries of champions
    countries = get_champion_countries(data)

    # Print champions and their win counts
    print("Wimbledon Champions:")
    for champion, count in sorted(champions.items()):
        print(f"{champion} {count}")

    # Print countries in alphabetical order
    print("\nThese {} countries have won Wimbledon:".format(len(countries)))
    print(", ".join(sorted(countries)))

if __name__ == "__main__":
    main()

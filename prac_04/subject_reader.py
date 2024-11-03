"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)


def load_data():
    """Read data from file formatted like: subject, lecturer, number of students."""
    data_list = []  # Initialize an empty list to hold each line's data
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Convert the student number to an integer
        data_list.append(parts)  # Add this line's data as a list to data_list
    input_file.close()
    return data_list  # Return the list of lists


main()

"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject, lecturer, number of students."""
    data_list = []  # Initialize an empty list to hold each line's data
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Convert the student number to an integer
            data_list.append(parts)  # Add this line's data as a list to data_list
    return data_list  # Return the list of lists


def display_subject_details(data):
    """Display details of each subject in a formatted output."""
    for subject, lecturer, student_count in data:
        print(f"{subject} is taught by {lecturer} and has {student_count} students")


main()

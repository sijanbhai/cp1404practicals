# emails.py

"""
Estimate Time: 45 minutes
Actual Time: 30 minutes

This program stores users' emails and names in a dictionary.
It asks for an email and then tries to extract the name from the email address.
The user can confirm or correct the extracted name.
When done, it prints out the email and associated name.

Functions:
- extract_name_from_email(email): Extracts and returns the name from an email.
"""


def extract_name_from_email(email):
    """
    Extracts the name from the email address by splitting the email at '@'
    and using the part before the '@' to generate a name.
    The name is capitalized and formatted by replacing '.' with a space.

    Args:
    email (str): The email address from which the name will be extracted.

    Returns:
    str: The formatted name extracted from the email.
    """
    local_part = email.split('@')[0]  # Get the part before the '@'
    name = local_part.replace('.', ' ').title()  # Replace dots with spaces and capitalize
    return name


def main():
    email_to_name = {}  # Dictionary to store email and corresponding name

    while True:
        email = input("Email: ").strip()

        if email == "":  # Exit the loop if the email is blank
            break

        # Extract the name from the email
        name = extract_name_from_email(email)

        # Ask the user if the extracted name is correct
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation not in ["", "y"]:  # If not 'Y' or blank, ask for the name
            name = input("Name: ").strip()

        # Store the email and name in the dictionary
        email_to_name[email] = name

    # Print all emails and names
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()

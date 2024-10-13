def main():
    MINIMUM_LENGTH = 8
    password = get_password(MINIMUM_LENGTH)

    # Call the function to print asterisks
    print_asterisks(password)


def get_password(minimum_length):
    """Prompt user for a password and check it meets the minimum length."""
    password = input(f"Enter a password (minimum {minimum_length} characters): ")

    # Check the password length and prompt again if it's too short
    while len(password) < minimum_length:
        print(f"Password is too short! It must be at least {minimum_length} characters.")
        password = input(f"Enter a password (minimum {minimum_length} characters): ")

    return password


def print_asterisks(password):
    """Print asterisks corresponding to the length of the password."""
    print('*' * len(password))


# Call the main function to execute the program
if __name__ == "__main__":
    main()

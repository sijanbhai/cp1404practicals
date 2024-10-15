def get_valid_score():
    """Get a valid score from the user (0-100 inclusive)."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Try again.")
        score = float(input("Enter score (0-100): "))
    return score


def get_score_result(score):
    """Determine the result based on the score."""
    if score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print as many stars as the score."""
    print('*' * int(score))


def main():
    MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print("Welcome to the Score Program!")

    # Get a valid score initially
    score = get_valid_score()

    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_score_result(score)
            print(f"Score: {score}, Result: {result}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell!")
        else:
            print("Invalid option, please choose from the menu.")


if __name__ == "__main__":
    main()

import random

def get_score_result(score):
    """Determine the result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = float(input("Enter score: "))
    result = get_score_result(score)
    print(result)

    # Generate a random score and print the result
    random_score = random.randint(0,100)
    print(f"Random score: {random_score}")
    random_result = get_score_result(random_score)
    print(random_result)

main()

import random

NUMBERS_PER_QUICK_PICK = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        # Print numbers in sorted order, each number right-aligned in a 2-character space
        print(" ".join(f"{number:2}" for number in sorted(quick_pick)))

def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_QUICK_PICK:
        number = random.randint(MINIMUM, MAXIMUM)
        # Only add unique numbers
        if number not in quick_pick:
            quick_pick.append(number)
    return quick_pick

main()

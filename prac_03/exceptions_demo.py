"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A Value error will occur if the user inputs a value for the numerator or denominator that cannot be converted to an integer. For example, entering a string like abc, a floating-point number like 2.5, or any non-numeric characters will raise a Value error.
2. When will a ZeroDivisionError occur?
When a user inputs 0 for the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, I can change the code to avoid the possibility of a ZeroDivisionError.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check for zero denominator before division
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

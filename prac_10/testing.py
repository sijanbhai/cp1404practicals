"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase(phrase):
    """
    Format a phrase as a sentence, starting with a capital letter and ending with a full stop.
    >>> format_phrase("hello")
    'Hello.'
    >>> format_phrase("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_phrase("this is a test")
    'This is a test.'
    """
    phrase = phrase.strip()  # Remove any leading/trailing spaces
    if not phrase.endswith("."):
        phrase += "."  # Ensure the phrase ends with a single full stop
    return phrase[0].upper() + phrase[1:]  # Capitalize the first letter


def run_tests():
    """Run the tests on the functions."""
    # Test repeat_string
    assert repeat_string("Python", 1) == "Python", "repeat_string failed for n=1"
    assert repeat_string("hi", 2) == "hi hi", "repeat_string failed for n=2"

    # Test Car's fuel setting
    car = Car()  # Default fuel
    assert car._fuel == 0, "Car does not set fuel correctly (default)"

    car = Car(fuel=10)  # Custom fuel
    assert car._fuel == 10, "Car does not set fuel correctly (custom)"


run_tests()
doctest.testmod()

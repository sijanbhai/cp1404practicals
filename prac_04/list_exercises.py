def main():
    numbers = []

    # Prompt the user to enter 5 numbers and store each in the list
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)

    # Display the required information
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


main()

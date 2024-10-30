# Task 1
name = input("What is your name? ")
file = open('name.txt', 'w')
file.write(name)
file.close()

# Task 2
file = open('name.txt', 'r')
name_from_file = file.readline().strip()
file.close()
print(f"Hi {name_from_file}!")

# Task 3
with open('numbers.txt', 'r') as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())
    result = first_number + second_number
    print(result)

# Task 4
with open('numbers.txt', 'r') as file:
    total = 0
    for line in file:
        total += int(line.strip())
    print(total)
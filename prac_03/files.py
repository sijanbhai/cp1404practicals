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
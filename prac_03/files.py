# Task 1
name = input("What is your name? ")
file = open('name.txt', 'w')
file.write(name)
file.close()
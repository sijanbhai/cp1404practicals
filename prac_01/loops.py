print("a. Count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()
print("b. Count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()
n = int(input("c. Enter number of stars: "))
print("c. Print stars on one line:")
for i in range(n):
    print('*', end='')
print()
print("d. Print lines of increasing stars:")
for i in range(1, n + 1):
    print('*' * i)

rows = int(input("Enter the number of rows: "))

num = 1

for line in range(1, rows + 1):
    for other in range(line):
        print(num, end=" ")
        num += 1
    print()
size = int(input("Enter the size of the pattern: "))
j = 1
while j <= size:
    for i in range(size):
        print("*", end="")
    j += 1
    print()
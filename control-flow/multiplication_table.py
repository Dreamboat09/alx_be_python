number = int(input("Enter a number to see its multiplication table: "))
for num in range(1, 11):
    ans = number * num
    print(f"{number} * {num} = {ans}")
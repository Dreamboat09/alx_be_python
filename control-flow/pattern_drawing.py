size = int(input('Enter the size of the pattern: '))
star = 0
while star < size:
    for i in range(size):
        print('*', end='')
    print()
    star = star +1
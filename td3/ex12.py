N = int(input("Enter N: "))

for i in range(2, N + 1):
    premier = True

    for j in range(2, i):
        if i % j == 0:
            premier = False

    if premier:
        print(i)
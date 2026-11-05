H = int(input("Enter H: "))
for i in range(1, H + 1):
    for j in range(i):
        print("*", end="")
    print()
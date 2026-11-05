n = int(input("Enter a positive integer: "))

temp = n
s = 0

while temp > 0:
    chiffre = temp % 10

    fact = 1
    i = 1

    while i <= chiffre:
        fact = fact * i
        i = i + 1

    s = s + fact
    temp = temp // 10

if s == n:
    print("The number is equal to the sum of factorials")
else:
    print("The number is not equal to the sum of factorials")
import math

a = float(input("Donner a : "))
b = float(input("Donner b : "))
c = float(input("Donner c : "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Une infinité de solutions")
        else:
            print("Aucune solution")
    else:
        x = -c / b
        print("Solution unique :", x)

else:
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)

        print("Deux solutions réelles :")
        print("x1 =", x1)
        print("x2 =", x2)

    elif delta == 0:
        x = -b / (2*a)
        print("Une solution double :", x)

    else:
        print("Aucune solution réelle")
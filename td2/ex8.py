a = int(input("Donner le premier entier : "))
b = int(input("Donner le deuxième entier : "))

if b > a:
    a = b

b = int(input("Donner le troisième entier : "))

if b > a:
    a = b

b = int(input("Donner le quatrième entier : "))

if b > a:
    a = b

print("Le plus grand nombre est :", a)
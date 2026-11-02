chaine = input("Donner une chaîne : ")

inverse = ""

for i in range(len(chaine) - 1, -1, -1):
    inverse = inverse + chaine[i]

print("La chaîne inversée est :", inverse)
ch = input("Enter a string: ")

resultat = ""

for lettre in ch:
    if lettre not in resultat:
        resultat = resultat + lettre

print(resultat)

chaine = input("Entrez une chaîne : ")
chaine = chaine.replace(" ", "").lower()

if chaine == chaine[::-1]:
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")
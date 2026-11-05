nom1 = input("Donner le nom de la première personne : ")
age1 = int(input("Donner son âge : "))

nom2 = input("Donner le nom de la deuxième personne : ")
age2 = int(input("Donner son âge : "))

nom3 = input("Donner le nom de la troisième personne : ")
age3 = int(input("Donner son âge : "))

if age1 >= age2 and age1 >= age3:
    print("La personne la plus âgée est :", nom1)

elif age2 >= age1 and age2 >= age3:
    print("La personne la plus âgée est :", nom2)

else:
    print("La personne la plus âgée est :", nom3)
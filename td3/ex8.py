a=input("Donner une chaîne : ")
b=input("Donner un caractère : ")
c=0
for i in a:
    if i==b:
        c=c+1
print("Le caractère",b,"apparaît",c,"fois dans la chaîne.") 
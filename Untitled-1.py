
N = int(input("Donner un entier naturel N : "))
while N <= 0:
    N = int(input("Erreur ! Donner un entier strictement positif : "))
S = 0
for i in range(1, N + 1):
    S = S + 1/i
print("La somme S =", S)
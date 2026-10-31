
N = int(input("Donner un entier : "))
if N == 0:
    print("Le nombre de chiffres est : 1")
else:
    N = abs(N)
    C = 0
    while N > 0:
        N = N // 10
        C = C + 1
    print("Le nombre de chiffres est :", C)
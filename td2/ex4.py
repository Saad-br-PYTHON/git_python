a=int(input("Enter a number: "))
s=1
b=0
while s<a:
    if a%s==0:
        b=b+s
    s=s+1
if b==a:
    print("The number is perfect")
else:
    print("The number is not perfect")
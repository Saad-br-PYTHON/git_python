a=int(input("Enter a number: "))
c=0
if a==0:
    print('1')
 
else:
    while a!=0:
        a=a//10
        c=c+1
print('The number of digits in the number is:', c)
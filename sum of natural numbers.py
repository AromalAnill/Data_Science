n=int(input("enter any number:"))
if n<0:
    print("is positive number.")
else:
    sum=0
    while(n>0):
        sum+=n
        n-=1
    print("sum of natural numbers is:",sum)
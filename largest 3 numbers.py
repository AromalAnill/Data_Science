a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
c=float(input("Enter the third number:"))
if(a>b)and(a>c):
    print(a,"is largest number.")
elif(b>a)and(b>c):
    print(b,"is largest number.")
else:
    print(c,"is largest number.")
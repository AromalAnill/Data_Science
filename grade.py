def calculate(m1,m2,m3):
    tm=m1+m2+m3
    p=tm/3

    if tm >= 90:
        grade="A"
    elif tm >=80:
        grade="B"
    elif tm >=70:
        grade = "C"
    elif tm >=60:
        grade = "D"
    else:
        grade = "F"


    print("Total Marks:",tm)
    print("Percentage: ",p)
    print("Grade:",grade)

m1=int(input("Enter the mark 1:"))
m2=int(input("Enter the mark 2:"))
m3=int(input("Enter the mark 3:"))
calculate(m1,m2,m3)
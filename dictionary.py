student={}
name=input("Enter Student Name: ")
age=int(input("Enter Age: "))
student["name"]=name
student["age"]=age

print("Dictionary:",student)
key=input("Enter Key: ")
value=input("Enter Value: ")
student[key]=value
print("After adding:",student)
student["Age"]=int(input("Enter New Age: "))
print("After adding:",student)
key=input("Enter Key to remove: ")
del student[key]
print("After removing:",student)
print("Key value pairs:")
for k,v in student.items():
    print(k,":",v)

my_list = []
n = int(input("Enter number of elements: "))

for i in range(n):
    element = input("Enter an element: ")
    my_list.append(element)

print("Original list:", my_list)

add_element = input("Enter element to add: ")
my_list.append(add_element)

print("List after adding:", my_list)

remove_element = input("Enter element to remove: ")

if remove_element in my_list:
    my_list.remove(remove_element)
    print("List after removing:", my_list)
else:
    print("Element not found!")

print("Final list:", my_list)
import numpy as np


r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter the matrix elements:")

A= []
for i in range(r):
    A.append(list(map(int, input().split())))

A = np.array(A)

print("\n___Matrix___")
print(A)

print("\n___Statistics___")
print("Sum  :", np.sum(A))
print("Mean :", np.mean(A))
print("Max  :", np.max(A))
print("Min  :", np.min(A))

print("\n___Flipping___")
print("\nLeft to Right Flip (Horizontal)")
print(np.fliplr(A))

print("\nUp to Down Flip (Vertical)")
print(np.flipud(A))

print("\n___Rotation___")
print("\n90° Rotation (Counterclockwise)")
print(np.rot90(A))

print("\n180° Rotation")
print(np.rot90(A, 2))

print("\n270° Rotation (Counterclockwise)")
print(np.rot90(A, 3))
import numpy as np
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])

print("\nMatrix A")
print(A)

print("\nMatrix B")
print(B)

print("\nAddition")
print(A+B)

print("\nSubtraction")
print(A-B)

print("\nMultiplication")
print(A*B)

print("\nDivision")
print(A/B)

print("\nTranspose ")
print("A=")
print(A.T)
print("B=")
print(B.T)

print("\nDeterminant")
print("A=",np.linalg.det(A))
print("B=",np.linalg.det(B))

print("\nInverse")
print("A=")
print(np.linalg.inv(A))
print("B=")
print(np.linalg.inv(B))

print("\nReshape")
print("A (1*4)=")
print(A.reshape((1,4)))

print("B (1*4)=")
print(B.reshape((1,4)))
#Find the duplicate number on a given integer array


A = [1,3,2,4,5,6,7,8,9,2,3,1,4]
B = set(A)
print(A)
print(B)
C = set(A ^ B)
print(C)

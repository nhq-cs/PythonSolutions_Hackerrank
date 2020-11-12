import numpy as np
n = int(input())
arr1 = []
arr2 = []
for i in range(n):
    temp1 =list(map(int, input().split()))
    arr1.append(temp1)
for i in range(n):
    temp2 =list(map(int, input().split()))
    arr2.append(temp2)
print(np.dot(arr1,arr2))

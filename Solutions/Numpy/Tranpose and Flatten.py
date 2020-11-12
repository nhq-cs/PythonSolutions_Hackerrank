import numpy as np
row, column = map(int, input().split())
a= []
for i in range(row):
    temp = list(map(int, input().split()))
    a.append(temp)
arr = np.array(a)
print(arr.transpose())
print(arr.flatten())

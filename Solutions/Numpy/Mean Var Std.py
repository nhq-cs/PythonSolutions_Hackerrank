import numpy as np
np.set_printoptions(sign = ' ')
row, column = map(int, input().split())
arr = []
for i in range(row):
    temp = list(map(int,input().split()))
    arr.append(temp)
arr = np.array(arr).reshape(row,column)
print(np.mean(arr,axis=1))
print(np.var(arr,axis =0))
std = np.std(arr,axis=None)
print(round(std,12))

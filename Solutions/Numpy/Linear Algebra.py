import numpy as np
arr = []
n = int(input())
for i in range(n):
    temp = list(map(float, input().split()))
    arr.append(temp)
answer = round(np.linalg.det(arr),2)
print(answer)

import numpy as np 
a,b  =map(int, input().split())
arr = []
answer = 1 
for i in range(a):
    temp = list(map(int, input().split()))
    arr.append(temp)
save = np.sum(arr, axis=0)
for item in save:
    answer *= item
print(answer)

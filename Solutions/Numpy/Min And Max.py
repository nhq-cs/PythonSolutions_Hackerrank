import numpy as np
a= []
answer = []
row, column = map(int, input().split())
for i in range(row):
    temp = list(map(int, input().split()))
    a.append(temp)
arr = np.array(a, dtype='int')
for item in np.min(arr, axis =1):
    answer.append(item)
print(max(answer))

import numpy as np
n,m,p = map(int, input().split())
a= []
for i in range(n+m):
    temp = list(map(int, input().split()))
    a.append(temp)
answer = np.array(a).reshape(n+m, p)
print(answer)

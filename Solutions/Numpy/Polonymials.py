import numpy as np
cof = list(map(float, input().split()))
x = float(input())
print(np.polyval(cof,x))

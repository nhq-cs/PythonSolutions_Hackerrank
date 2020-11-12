import numpy as np
np.set_printoptions(sign = ' ')
row, column = map(int, input().split())
print(np.eye(row,column,k=0))

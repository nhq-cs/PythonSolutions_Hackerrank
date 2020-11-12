import numpy as np
np.set_printoptions(sign=' ')
arr = np.array(input().split(),dtype=float)
print(np.floor(arr),np.ceil(arr),np.rint(arr),sep='\n')

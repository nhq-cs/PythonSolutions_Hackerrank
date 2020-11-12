import numpy as np
arr1 = np.array([[input().split()]],dtype='int')
arr2 = np.array([[input().split()]],dtype='int')
inner = np.inner(arr1,arr2)
print(int(inner))
print(np.outer(arr1,arr2))

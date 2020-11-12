import numpy

def arrays(arr):
    answer = numpy.array(arr,dtype=float)
    return answer[::-1]
arr = input().strip().split(' ')
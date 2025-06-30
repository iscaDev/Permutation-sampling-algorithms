import numpy

def numpy_implementation(arr):
    return numpy.random.permutation(arr)

arrInput=list(input().split())
print(numpy_implementation(arrInput))
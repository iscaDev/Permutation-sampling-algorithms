import time
import matplotlib.pyplot as plt
import numpy
import random

#My implementation of Fisher-Yates algorithm
def fisher_yates(array):
    n=len(array)
    for i in range(n-1, 0, -1):  
        
        j=random.randint(0, i) 
        

        array[i],array[j] = array[j],array[i]

    return array 

#NumPy permutation algorithm
def numpy_implementation(arr):
    return numpy.random.permutation(arr)



sizes = [100, 1000, 5000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000] # different sizes to test the algorithms on
fisher_times = []
numpy_times = []

for size in sizes:
    arr = list(range(size))

    # Fisher-Yates implementation 
    start = time.time()
    fisher_yates(arr[:])
    fisher_times.append((time.time() - start)*1000)

    # NumPy implementation
    arr_np = numpy.array(arr)
    start = time.time()
    numpy_implementation(arr_np)
    numpy_times.append((time.time() - start)*1000)

#Here to plot the comparison of their execution time
plt.plot(sizes, fisher_times, label='Fisher-Yates', marker='o')
plt.plot(sizes, numpy_times, label='NumPy Implementation', marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (milliseconds)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


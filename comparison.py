import time
import matplotlib.pyplot as plt
import numpy
import random

def fisher_yates(array):
    n=len(array)
    for i in range(n-1, 0, -1):  # from n-1 to 0 as array indexes start from 0, not 1
        
        j=random.randint(0, i) # random index from 0 to i-1, because element cannot be swapped with itself
        
        # swap array[i] with the element at randomly selected index
        array[i],array[j] = array[j],array[i]

    return array 


def numpy_implementation(arr):
    return numpy.random.permutation(arr)



sizes = [100, 1000, 5000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
fisher_times = []
numpy_times = []

for size in sizes:
    arr = list(range(size))

    # Fisher-Yates implementation 
    start = time.time()
    fisher_yates(arr[:])
    fisher_times.append(time.time() - start)

    # NumPy implementation
    arr_np = numpy.array(arr)
    start = time.time()
    numpy_implementation(arr_np)
    numpy_times.append(time.time() - start)

plt.plot(sizes, fisher_times, label='Fisher-Yates', marker='o')
plt.plot(sizes, numpy_times, label='NumPy Implementation', marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Permutation Sampling Execution-time Comparison')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


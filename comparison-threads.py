import numpy as np
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
import time
import random

# Permutation methods
def argsort_uniform(arr):
    return arr[np.argsort(np.random.rand(len(arr)))]

def parallel_argsort(arr, nthreads):
    n = len(arr)
    keys = np.random.rand(n)
    bucket_ids = np.random.randint(0, nthreads, size=n)

    def sort_bucket(bucket_id):
        mask = (bucket_ids == bucket_id)
        idx = np.nonzero(mask)[0]
        if len(idx) == 0:
            return np.array([], dtype=int)
        return idx[np.argsort(keys[idx])]

    with ThreadPoolExecutor(max_workers=nthreads) as executor:
        futures = [executor.submit(sort_bucket, i) for i in range(nthreads)]
        sorted_chunks = [f.result() for f in futures]

    idx = np.concatenate(sorted_chunks)
    return arr[idx]

def fisher_yates(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]

# Benchmark function
def benchmark(method, arr, nthreads=1, repeat=30):
    times = []
    for _ in range(repeat):
        start = time.perf_counter()
        if method == "numpy_permutation":
            np.random.permutation(arr)
        elif method == "argsort_uniform":
            argsort_uniform(arr)
        elif method == "parallel":
            parallel_argsort(arr, nthreads)
        elif method == "fisher_yates":
            fisher_yates(arr)
        end = time.perf_counter()
        times.append((end - start) * 1000)  # convert to ms
    return np.average(times)

# Parameters
sizes = np.arange(start=10000, stop=101000, step=10000)
threads = [1, 2, 4, 8, 16] # can be changed depending on the CPU

# Run benchmark
results_parallel = {t: [] for t in threads}
results_numpy = []
results_argsort = []
results_fy = []

for n in sizes:
    base_arr = np.arange(n)

    # NumPy permutation
    t_np = benchmark("numpy_permutation", base_arr)
    results_numpy.append(t_np)

    # Argsort of uniform
    t_as = benchmark("argsort_uniform", base_arr)
    results_argsort.append(t_as)

    # Fisher-Yates
    t_fy = benchmark("fisher_yates", base_arr)
    results_fy.append(t_fy)

    # Parallel
    for t in threads:
        t3 = benchmark("parallel", base_arr, nthreads=t)
        results_parallel[t].append(t3)



# Plotting 
plt.plot(sizes, results_numpy, label="NumPy permutation",
         linestyle='--', marker='x', linewidth=1, markersize=4, color='black')

plt.plot(sizes, results_argsort, label="Argsort of uniform",
         linestyle=':', marker='d', linewidth=1, markersize=4, color='gray')

# Fisher-Yates is not displayed as it is scaling up the plot
# plt.plot(sizes, results_fy, label="Fisher-Yates",
#           linestyle='-', marker='s', linewidth=1, markersize=4, color='green')

# Threaded implementations
for t in threads:
    plt.plot(sizes, results_parallel[t], label=f'{t} threads',
             linestyle='-', marker='o', linewidth=1, markersize=4)

plt.xlabel('Array size (n)', fontsize=10)
plt.ylabel('Time (ms)', fontsize=10)
plt.title('Benchmark: Random Permutation Methods', fontsize=12)

plt.legend(fontsize=8)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()





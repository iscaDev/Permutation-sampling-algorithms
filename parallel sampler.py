import numpy as np
import time
import matplotlib.pyplot as plt

# core function for one permutation

def uniform_sort_sampler(n):
    # generate uniform random numbers
    random_values = np.random.uniform(0, 1, size=n)
    
    # sort and get the permutation (of indices)
    permutation = np.argsort(random_values) 
    
    return permutation


# benchmarking over multiple runs

def benchmark_sampler(n, runs):
    times = []

    for i in range(runs):
        start = time.perf_counter()
        uniform_sort_sampler(n)
        end = time.perf_counter()
        times.append((end - start)*1000)
    
    return np.array(times)

# plotting the results


def plotting(sizes, runs=100): # runs 100 times over each permutation size, n
    means = []
    errors = []

    for n in sizes:
        times = benchmark_sampler(n, runs)
        mean = np.mean(times)
        stderr = np.std(times, ddof=1) / np.sqrt(runs)
        ci = 1.96 * stderr
        means.append(mean)
        errors.append(ci)

    plt.errorbar(sizes, means, yerr=errors, fmt='-o', capsize=8)
    plt.xlabel('Permutation size (n)')
    plt.ylabel('Mean execution time (milliseconds)')
    plt.title('Mean execution time with 95% confidence interval')
    plt.grid(True)
    plt.show()
    

# plotting a histogram for a fixed size, m

def plot_histogram_for_size(m, runs=100):
    times = benchmark_sampler(m, runs)
    
    plt.hist(times, bins=30, edgecolor='black')
    plt.xlabel('Execution time (milliseconds)')
    plt.ylabel('Frequency')
    plt.title(f'Execution time distribution for n = {m}')
    plt.grid(True)
    plt.show()
 
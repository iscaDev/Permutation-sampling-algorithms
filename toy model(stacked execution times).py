import numpy as np
import time
import matplotlib.pyplot as plt


def uniform_sampling(n):
    # generate uniform random numbers
    global random_values
    random_values = np.random.uniform(0, 1, size=n)

def uniform_sorting(random_values):
    # sort and get the permutation (of indices)
    permutation = np.argsort(random_values) 
    
    return permutation


# benchmarking over multiple runs

def benchmark_sampler(n, runs):
    sampling_times = []
    sorting_times = []
    for i in range(runs):
        # Time sampling
        start_sampling = time.perf_counter()
        uniform_sampling(n)
        end_sampling = time.perf_counter()
        sampling_time = (end_sampling - start_sampling) * 1000  # ms
        # Time sorting
        start_sorting = time.perf_counter()
        uniform_sorting(random_values)  # Default is quicksort
        end_sorting = time.perf_counter()
        sorting_time = (end_sorting - start_sorting) * 1000  # ms

        sampling_times.append(sampling_time)
        sorting_times.append(sorting_time)

    return np.array(sampling_times), np.array(sorting_times)


# plotting the split of execution time

def stacked_bar_plot(sizes, runs=100):
    sampling_means = []
    sorting_means = []

    for n in sizes:
        sampling, sorting = benchmark_sampler(n, runs)
        sampling_means.append(np.mean(sampling))
        sorting_means.append(np.mean(sorting))

    x = np.arange(len(sizes))
    width = 0.5

    plt.bar(x, sampling_means, width, label='Sampling', color='skyblue')
    plt.bar(x, sorting_means, width, bottom=sampling_means, label='Sorting', color='orange')

    plt.xlabel('Permutation size (n)')
    plt.ylabel('Mean execution time (ms)')
    plt.title(f'Stacked execution times (Sampling + Sorting) over {runs} runs')
    plt.xticks(x, sizes)
    plt.legend()
    plt.grid(False)
    plt.tight_layout()
    plt.show()
    

import random

# Quick-Shuffle

def quick_shuffle(arr):
    n = len(arr)
    if n <= 1:
        return arr

    # Generate n random bits in one go
    bits = random.getrandbits(n)
    
    left, right = [], []
    for i in range(n):
        bit = (bits >> i) & 1  # Extract i-th bit from the right
        if bit == 0:
            left.append(arr[i])
        else:
            right.append(arr[i])

    # Recursively shuffle both sides
    return quick_shuffle(left) + quick_shuffle(right)
#Implementation of the Fisher-Yates algorithm in Python
import random
#following is a function to generate random permutation of an array[]
def fisher_yates(array):
    n=len(array)
    for i in range(n-1, 0, -1):  
        
        j=random.randint(0, i) # random index from 0 to i-1
        
        # swap array[i] with the element at randomly selected index
        array[i],array[j] = array[j],array[i]

    return array

# user can input a sequence with a whitespace between its elements
arrInput=list(input().split())

print(fisher_yates(arrInput)) # outputs the returned shuffle from the fisher_yates function above

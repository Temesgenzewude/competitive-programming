
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    counts=[0 for _ in range(100)]
    for element in arr:
        counts[element]+=1
    return counts
 

def LinearSearch(A, low, high, key):
    if A[low] == key:
        return low
    else:
        LinearSearch(A, low+1, high, key)

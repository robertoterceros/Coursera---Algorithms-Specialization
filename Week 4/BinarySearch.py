def BinarySearch(A, low, high, key):
    if high < low:
        return (low - 1)
    mid = (low + (high - low)/2) %Parte entera hacia abajo o the floor
    if A[mid] == key:
        return mid
    else if key < A[mid]:
        return BinarySearch(A, low, mid - 1, key)
    else if key > A[mid]:
        return BinarySearch(A, mid + 1, high, key)

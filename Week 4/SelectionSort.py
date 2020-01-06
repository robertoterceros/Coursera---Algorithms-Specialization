def SelectionSort(A):
    for i in range(len(A)):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        A[i], A[minIndex] = A[minIndex], A[i]
    return A

def MergeSort(A):
    if n == 1:
        return A
    m = (n/2).round(0)
    B = MergeSort(A[:m])
    C = MergeSort(A[m:])
    A_prima = Merge(B,C)
    return A_prima

def Merge(B,C):
    #TODO   

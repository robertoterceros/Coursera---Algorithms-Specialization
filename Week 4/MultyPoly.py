def MultPoly(A, B, n):
    import numpy as np
    product = np.array(2*n-1,)
    for i in range(2*n-1):
        product[i] = 0
    for i in range(n-1):
        for j in range(n-1):
            product[i+j] = product[i+j] + A[i]*B[j]


def Mult2(A, B, n, a1, b1):
    R = np.array(2*n)
    if n == 1:
        R[0] = A[a1]*B[b1]
        return R
    R[range(n-2),-] = Mult2(A, B, n/2, a1, b1)
    R[-,range(n,2*n-2)] = 

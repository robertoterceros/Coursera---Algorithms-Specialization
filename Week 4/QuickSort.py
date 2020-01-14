def quick_sort(A):
    """
    Pasar la lista A
    """
    quick_sort2(A, 0, len(A)-1)

def quick_sort2(A, izquierda, derecha):
    if izquierda < derecha:
        p = particion(A, izquierda, derecha)
        quick_sort2(A, izquierda, p-1)
        quick_sort2(A, p+1, derecha)

def obtener_pivote(A, izquierda, derecha):
    medio = (izquierda + derecha) // 2
    pivote = medio
    if A[izquierda] < A[medio]:
        if A[pivote] < A[derecha]:
            pivote = medio
    elif A[izquierda] < A[derecha]:
        pivote = izquierda
    return pivote

def particion(A, izquierda, derecha):
    pivoteIndex = obtener_pivote(A, izquierda, derecha)
    pivoteValue = A[pivoteIndex]
    A[pivoteIndex], A[izquierda] = A[izquierda], A[pivoteIndex]
    borde = low

    for i in range(izquierda, derecha + 1):
        if A[i] < pivoteValue:
            borde += 1
            A[i], A[borde] = A[borde], A[i]
        A[izquierda], A[borde] = A[borde], A[izquierda]

    return (borde)

# Assume x1 < x2 < ... < xn


def PointsCoverSorted(x):
    # Definir el conjunto R
    n = len(x)
    R = set()
    i = 0
    while i < n:
        (l, r) = (x[i], x[i]+1)
        R = R.union((l, r))
        print(R)
        i += 1
        while i < n and x[i] <= r:
            i = i + 1
    return R

if __name__ == '__main__':
    lista = list([5, 5.5, 5.8, 6, 7])
    a = PointsCoverSorted(lista)
    print(a)

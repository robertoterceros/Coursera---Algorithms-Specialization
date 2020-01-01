def knapsack(W, weights, values):
    n = len(weights)
    A = np.zeros(n,)
    V = 0
    for i in range(n):
        if W == 0:
            return(V, A)
        a = min(weights[i], W)
        V = V + a * values[i]/weights[i]
        weights[i] = weights[i] - a
        A[i] = A[i] + a
        W = W - a
    return (V, A)

if __name__ == "__main__":
    import numpy as np
    weights = [1, 2, 3, 4]
    values = [2, 2, 4, 5]
    W = 9
    respuesta = knapsack(W, weights, values)
    print(respuesta)

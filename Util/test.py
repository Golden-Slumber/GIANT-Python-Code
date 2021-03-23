import numpy as np

if __name__ == '__main__':
    a = np.array([[0, 1, 2], [1, 2, 3], [3, 4, 5], [1, 2, 3]])
    b = np.array([[2], [2], [2], [2]])
    print(a.shape)
    print(b.shape)
    print(np.multiply(a, b))

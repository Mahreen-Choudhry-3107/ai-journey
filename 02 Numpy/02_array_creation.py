import numpy as np

print(np.array([1, 2, 3]))          # [1 2 3]
print(np.zeros((2, 3)))             # 2x3 of 0.
print(np.ones((2, 2)))              # 2x2 of 1.
print(np.full((2, 2), 7))           # [[7 7] [7 7]]
print(np.empty((2, 2)))             # garbage values
print(np.arange(0, 10, 2))          # [0 2 4 6 8]
print(np.linspace(0, 1, 5))         # [0. 0.25 0.5 0.75 1.]
print(np.logspace(0, 2, 3))         # [1. 10. 100.]
print(np.eye(3))                    # identity matrix
print(np.diag([1, 2, 3]))           # diagonal matrix
print(np.zeros_like(np.ones((2, 2))))

x, y = np.meshgrid([1, 2, 3], [10, 20])
print(x)  # [[1 2 3] [1 2 3]]
print(y)  # [[10 10 10] [20 20 20]]

print(np.fromfunction(lambda i, j: i + j, (3, 3)))
print(np.fromiter((i * i for i in range(5)), dtype=int))  # [0 1 4 9 16]
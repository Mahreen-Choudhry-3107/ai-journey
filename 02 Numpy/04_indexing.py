import numpy as np

a = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

print(a[0])            # [10 20 30]
print(a[1, 2])         # 60
print(a[:, 0])         # [10 40 70]
print(a[0:2, 1:3])     # [[20 30] [50 60]]
print(a[::-1])         # rows reversed
print(a[-1, -1])       # 90

# boolean
print(a[a > 50])       # [60 70 80 90]

# fancy
print(a[[0, 2]])       # rows 0 and 2
print(a[[0, 1], [1, 2]])   # [20 60]

# where
print(np.where(a > 50, 1, 0))
print(np.nonzero(a > 50))
print(np.argwhere(a > 80))         # [[2 2]]

# newaxis and ellipsis
v = np.array([1, 2, 3])
print(v[:, np.newaxis].shape)      # (3, 1)
print(a[..., 0])                   # same as a[:, 0]

# take / put
print(np.take(v, [0, 2]))          # [1 3]
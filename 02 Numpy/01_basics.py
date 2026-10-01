# FILE: 01_basics.py
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)     # (2, 3)
print(a.ndim)      # 2
print(a.size)      # 6
print(a.dtype)     # int64
print(a.itemsize)  # 8 (bytes per element)
print(a.nbytes)    # 48

# list vs array
lst = [1, 2, 3]
arr = np.array(lst)
print(lst * 2)     # [1, 2, 3, 1, 2, 3]  (repeats)
print(arr * 2)     # [2 4 6]             (element-wise)
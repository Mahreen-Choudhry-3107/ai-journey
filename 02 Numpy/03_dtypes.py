# FILE: 03_dtypes.py
import numpy as np

a = np.array([1, 2, 3], dtype=np.int8)
print(a.dtype)                      # int8
b = a.astype(float)
print(b)                            # [1. 2. 3.]

# overflow
x = np.array([127], dtype=np.int8)
print(x + 1)                        # [-128]  (wraps around!)

print(np.iinfo(np.int32).max)       # 2147483647
print(np.finfo(np.float64).eps)     # 2.22e-16

print(np.result_type(np.int32, np.float64))   # float64
print(np.can_cast(np.int64, np.int8))         # False

c = np.array([1+2j, 3+4j])
print(c.real, c.imag)               # [1. 3.] [2. 4.]
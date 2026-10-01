import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(np.concatenate([a, b], axis=0))   # 4x2
print(np.concatenate([a, b], axis=1))   # 2x4
print(np.vstack([a, b]))
print(np.hstack([a, b]))
print(np.stack([a, b]).shape)           # (2, 2, 2) new axis
print(np.column_stack([[1, 2], [3, 4]]))

x = np.arange(6)
print(np.split(x, 3))                   # [array([0,1]), array([2,3]), array([4,5])]
print(np.array_split(x, 4))             # uneven allowed
print(np.hsplit(np.arange(8).reshape(2, 4), 2))
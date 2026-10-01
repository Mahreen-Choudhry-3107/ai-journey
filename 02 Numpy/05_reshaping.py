import numpy as np

a = np.arange(6)                    # [0 1 2 3 4 5]
print(a.reshape(2, 3))
print(a.reshape(3, -1))             # -1 auto-calculates (3,2)

m = a.reshape(2, 3)
print(m.T)                          # transpose (3,2)
print(m.flatten())                  # copy
print(m.ravel())                    # view if possible

v = np.array([1, 2, 3])
print(np.expand_dims(v, 0).shape)   # (1, 3)
print(np.squeeze(np.ones((1, 3, 1))).shape)   # (3,)

print(np.flip(v))                   # [3 2 1]
print(np.roll(v, 1))                # [3 1 2]
print(np.rot90(m))
print(np.repeat(v, 2))              # [1 1 2 2 3 3]
print(np.tile(v, 2))                # [1 2 3 1 2 3]
print(np.pad(v, 1, constant_values=0))   # [0 1 2 3 0]
print(np.append(v, 4))              # [1 2 3 4]
print(np.insert(v, 1, 99))          # [1 99 2 3]
print(np.delete(v, 0))              # [2 3]
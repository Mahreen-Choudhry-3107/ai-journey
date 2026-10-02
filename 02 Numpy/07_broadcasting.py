import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])         # (2,3)
b = np.array([10, 20, 30])        # (3,)
print(a + b)                      # b stretched across rows

col = np.array([[1], [2]])        # (2,1)
print(a + col)                    # col stretched across columns

x = np.array([[1], [2], [3]])     # (3,1)
y = np.array([10, 20, 30])        # (3,)
print(x + y)                      # (3,3) grid

# error case
try:
    np.ones((3, 2)) + np.ones(3)
except ValueError as e:
    print("Error:", e)

print(np.broadcast_to([1, 2, 3], (2, 3)))
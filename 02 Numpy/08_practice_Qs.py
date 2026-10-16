import numpy as np
# Create a 1D array of numbers 0 to 19, then reshape it into a 4×5 matrix.

arr = np.arange(20).reshape(4, 5)
print(arr)


# Create a 5×5 matrix with 1s on the border and 0s inside.

matrix = np.ones((5, 5))
matrix[1:4, 1:4] = 0
print(matrix)

# Create 10 random integers between 1 and 100. Print the max, min, and the index of the max.
random_integers = np.random.randint(1, 101, 10)
print("Random Integers:", random_integers)
print("Max:", np.max(random_integers))
print("Min:", np.min(random_integers))
print("Index of Max:", np.argmax(random_integers))
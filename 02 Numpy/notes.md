import numpy as np


1) WHAT IS NUMPY?
-----------------
- library for fast number crunching
- main object = ndarray (n-dimensional array)
- faster than lists, uses less memory
- all elements same type


2) ARRAY ATTRIBUTES
-------------------
a = np.array([[1,2,3],[4,5,6]])

a.shape    -> (2,3)    rows, cols
a.ndim     -> 2        number of dimensions
a.size     -> 6        total elements
a.dtype    -> int64    data type
a.itemsize -> bytes per element


3) CREATING ARRAYS
------------------
np.array([1,2,3])
np.zeros((3,3))         all 0
np.ones((2,4))          all 1
np.full((2,2), 7)       all 7
np.empty((2,2))         uninitialized
np.arange(0,10,2)       0,2,4,6,8
np.linspace(0,1,5)      5 points from 0 to 1
np.eye(3)               identity matrix
np.random.rand(3,3)     random 0-1


4) DATA TYPES
-------------
int8, int16, int32, int64
float32, float64
bool, complex, str

a.astype(float)         change dtype
- watch out for overflow in small int types


5) INDEXING & SLICING
---------------------
a[0]            first row
a[1,2]          row 1, col 2
a[:,0]          all rows, col 0
a[0:2, 1:3]     sub-matrix
a[::-1]         reverse

Boolean indexing:
a[a > 3]        elements greater than 3

Fancy indexing:
a[[0,2,4]]      pick specific positions

- slicing = VIEW (shares memory)
- fancy/boolean = COPY


6) RESHAPING
------------
a.reshape(3,2)
a.reshape(-1,1)     -1 means "figure it out"
a.flatten()         copy, 1D
a.ravel()           view if possible, 1D
a.T                 transpose
np.expand_dims(a,0)
np.squeeze(a)       remove size-1 dims


7) JOINING & SPLITTING
----------------------
np.concatenate([a,b], axis=0)
np.vstack([a,b])       stack vertically
np.hstack([a,b])       stack horizontally
np.stack([a,b])        new axis

np.split(a, 3)
np.hsplit(a, 2)
np.vsplit(a, 2)


8) BROADCASTING
---------------
- lets arrays of different shapes work together
- rules (compare shapes from the RIGHT):
    1. dims equal -> ok
    2. one dim is 1 -> stretched
    3. else -> ERROR

example:
(3,3) + (3,)   ok
(3,1) + (1,3)  -> (3,3)
(3,2) + (3,)   ERROR


9) MATH (UFUNCS)
----------------
a + b, a - b, a * b, a / b, a ** 2   (element-wise)
np.sqrt(a)   np.exp(a)   np.log(a)
np.sin(a)    np.cos(a)
np.abs(a)    np.round(a)
np.floor(a)  np.ceil(a)

ufunc methods:
np.add.reduce(a)
np.add.accumulate(a)
np.multiply.outer(a,b)


10) STATISTICS / AGGREGATION
----------------------------
a.sum()     a.mean()     a.std()     a.var()
a.min()     a.max()
a.argmin()  a.argmax()   (index of min/max)
np.median(a)
np.percentile(a, 90)
np.cumsum(a)    np.cumprod(a)

axis rule:
axis=0 -> down columns
axis=1 -> across rows
keepdims=True keeps shape

NaN safe: np.nansum, np.nanmean, ...


11) SORTING & SEARCHING
-----------------------
np.sort(a)
np.argsort(a)           indices that would sort
np.unique(a)            unique values
np.unique(a, return_counts=True)
np.where(a > 3)         indices where true
np.where(a>3, 1, 0)     if-else for arrays
np.searchsorted(a, x)
np.isin(a, [1,2])
np.any(a)    np.all(a)
np.count_nonzero(a)


12) LINEAR ALGEBRA
------------------
a @ b  or  np.matmul(a,b)    matrix multiply
np.dot(a,b)
np.linalg.inv(a)             inverse
np.linalg.det(a)             determinant
np.linalg.solve(A,b)         solve Ax = b
np.linalg.eig(a)             eigenvalues/vectors
np.linalg.svd(a)
np.linalg.norm(a)
np.linalg.matrix_rank(a)
np.trace(a)
np.einsum(...)               flexible summation notation


13) RANDOM
----------
rng = np.random.default_rng(42)     (new way, seed 42)
rng.random(5)
rng.integers(0,10,size=5)
rng.normal(0,1,size=100)
rng.choice(a, size=3)
rng.shuffle(a)
rng.permutation(a)

- same seed = same numbers (reproducible)


14) MISSING VALUES
------------------
np.nan      np.inf
np.isnan(a)    np.isinf(a)
np.nan_to_num(a)
masked arrays -> np.ma


15) VIEW vs COPY
----------------
b = a[0:3]       view (changes affect a)
b = a.copy()     real copy
b.base           shows if it's a view


16) SAVING & LOADING
--------------------
np.save("f.npy", a)
np.load("f.npy")
np.savez("f.npz", a=a, b=b)
np.savetxt("f.csv", a, delimiter=",")
np.loadtxt("f.csv", delimiter=",")
np.genfromtxt("f.csv", delimiter=",")


17) POLYNOMIALS & FFT
---------------------
np.polyfit(x, y, deg)
np.polyval(coeffs, x)
np.roots(coeffs)

np.fft.fft(a)
np.fft.ifft(a)
np.fft.fftfreq(n)


18) DATES
---------
np.datetime64("2026-10-01")
np.timedelta64(5, "D")
np.arange("2026-01", "2026-06", dtype="datetime64[M]")


19) STRUCTURED ARRAYS
---------------------
dt = np.dtype([("name","U10"),("age","i4")])
x = np.array([("Ali",20),("Sara",22)], dtype=dt)
x["name"]


20) PERFORMANCE TIPS
--------------------
- avoid python for-loops -> use vectorization
- use out= to avoid temp arrays
- C-order (row) vs F-order (column) memory
- memmap for huge files
- np.lib.stride_tricks.sliding_window_view


21) INTEROP
-----------
pandas, scipy, matplotlib, scikit-learn,
pytorch, tensorflow, jax, numba, dask, cupy


22) COMMON MISTAKES
-------------------
- forgetting views share memory
- integer overflow
- comparing floats with == (use np.isclose)
- shape mismatch in broadcasting
- confusing axis=0 and axis=1
- using np.matrix (old, avoid)


23) PRACTICE IDEAS
------------------
- normalize data (z-score, min-max)
- linear regression from scratch
- moving average
- k-means from scratch
- image as array (grayscale, flip, crop)
- Game of Life
- Monte Carlo (estimate pi)

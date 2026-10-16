#  Series: series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index. A Series is like a fixed-size dictionary in that you can get and set values by index label.


import pandas as pd
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# iloc[], loc[]

print(s.iloc[0]) # Accessing the first element using iloc
print(s.loc['a']) # Accessing the first element using loc
print(s.iloc[1:4]) # Accessing elements from index 1 to 3 using iloc

#  All important methods in series
print(s.head()) # Display the first 5 elements
print(s.tail()) # Display the last 5 elements
print(s.shape) # Display the shape of the series
print(s.size) # Display the size of the series
print(s.ndim) # Display the number of dimensions of the series
print(s.dtype) # Display the data type of the series
print(s.index) # Display the index of the series
print(s.values) # Display the values of the series
print(s.index.name) # Display the name of the index


# Mathematical operations on series
print(s.sum()) # Display the sum of the series
print(s.mean()) # Display the mean of the series
print(s.std()) # Display the standard deviation of the series
print(s.min()) # Display the minimum value of the series
print(s.max()) # Display the maximum value of the series
print(s.median()) # Display the median of the series
print(s.mode()) # Display the mode of the series
#  DataFrame in Pandas is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object.

import pandas as pd

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df = pd.DataFrame(l, columns=['A', 'B', 'C'])

print(df)

# Accessing elements in DataFrame
print(df.iloc[0]) # Accessing the first row
print(df.loc[0]) # Accessing the first row using loc
print(df.iloc[0, 1]) # Accessing the element at first row and second column

# All important methods in DataFrame
print(df.head()) # Display the first 5 rows
print(df.tail()) # Display the last 5 rows
print(df.shape) # Display the shape of the DataFrame
print(df.size) # Display the size of the DataFrame
print(df.ndim) # Display the number of dimensions of the DataFrame
print(df.dtypes) # Display the data types of the columns


# Mathematical operations on DataFrame

print(df.sum()) # Display the sum of each column
print(df.mean()) # Display the mean of each column
print(df.median()) # Display the median of each column

# Example
data = {
   'Name' : ['Mahreen', 'Ayesha', 'Ali', 'Ahmed'],
   'Age' : [19, 20, 21, 22]
}

df = pd.DataFrame(data)
print(df)



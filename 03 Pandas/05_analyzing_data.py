""" One of the most used method for getting a quick overview of the DataFrame, is the head() method.

The head() method returns the headers and a specified number of rows, starting from the top.


"""
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head(4)) # Display the first 10 rows of the DataFrame
print(df.tail(3)) # Display the last 5 rows of the DataFrame


# Info about the data
print(df.info()) # Display a concise summary of the DataFrame
import pandas as pd

# Loading data from CSV file
df = pd.read_csv('data.csv')
print(df)


# Type
data = {
  'calories': [420, 380, 390],
  'duration': [50, 40, 45]
}
df = pd.DataFrame(data)
print(df.loc[0])
print(df.dtypes)
print(df.to_string())

# max rows

print(pd.options.display.max_rows) # Display the maximum number of rows to display

# Increase the number of rows to display
pd.options.display.max_rows = 100
print(pd.options.display.max_rows)
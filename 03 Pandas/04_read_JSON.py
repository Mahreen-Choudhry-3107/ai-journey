import pandas as pd

#  use read_json() function to read JSON file

# Dictionary as json
data = {
  "Name": ["Mahreen", "Ayesha", "Ali", "Ahmed"],
  "Age": [19, 20, 21, 22],
  "City": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
  "Country": ["Pakistan", "Pakistan", "Pakistan", "Pakistan"]
}

# Convert the dictionary to a JSON string
df = pd.DataFrame(data)
print(df)
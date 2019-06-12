import pandas as pd

# Read the csv file in
df = pd.read_csv('data_dictionary.csv')

# Save to file
df.to_html('data_dictionary.html')

# Assign to string
# htmTable = df.to_html()
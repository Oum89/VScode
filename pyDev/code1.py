import pandas as pd
import os
from tabulate import tabulate

path = format(os.environ['RootPath'])
file_path = path + '/pyProject/VScode/pyOutput/' + 'data.csv'
# Sample data for the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}

# Create the DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print("DataFrame:")
print(tabulate(df, headers='keys', tablefmt='psql'))

# Save the DataFrame to a CSV file

df.to_csv(file_path, sep='\t', index=False)

print(f"DataFrame saved to {file_path}")
>>>>>>> Stashed changes

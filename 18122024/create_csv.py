import pandas as pd

# Create sample data
data = {
    "Name": ["John Doe", "Jane Smith", "Alice Brown", "Bob White"],
    "Age": [28, 34, 26, 45],
    "Profession": ["Engineer", "Data Scientist", "Teacher", "Manager"],
    "Country": ["USA", "UK", "Canada", "Australia"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
file_path = "data.csv"
df.to_csv(file_path, index=False)
file_path

import pandas as pd

# Sample dataset
data = {
    'Name': ['John', 'Jane', 'Mike', 'Emma', 'Bob', 'Alice'],
    'Age': [25, 30, None, 35, 30, 28],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Salary': [50000, 60000, 45000, None, 55000, 65000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Handling missing values
print("\nHandling missing values:")
# Replace missing values in 'Age' and 'Salary' columns with mean values
mean_age = df['Age'].mean()
mean_salary = df['Salary'].mean()
df['Age'].fillna(mean_age, inplace=True)
df['Salary'].fillna(mean_salary, inplace=True)
print("Mean Age:", mean_age)
print("Mean Salary:", mean_salary)
print("\nDataFrame after handling missing values:")
print(df)

# Removing duplicates
print("\nRemoving duplicates:")
df.drop_duplicates(inplace=True)
print("DataFrame after removing duplicates:")
print(df)

# Data manipulation operations
# Filtering data
print("\nFiltering data (Age > 28):")
filtered_df = df[df['Age'] > 28]
print(filtered_df)

# Sorting data
print("\nSorting data (by Salary):")
sorted_df = df.sort_values(by='Salary', ascending=False)
print(sorted_df)

# Grouping data
print("\nGrouping data (mean by Gender):")
grouped_df = df.groupby('Gender').mean()
print(grouped_df)
import pandas as pd

# Read the CSV file
df = pd.read_csv('pdf tables.csv')

# Filter condition: Biology marks >= 71
filtered_df = df[df['Biology'] >= 71]

# Calculate total Maths marks
total_maths = filtered_df['Maths'].sum()

print(f"\nTotal Maths marks for students with Biology >= 71: {total_maths}")

# Display the filtered data for verification
print("\nFiltered student records (showing first 10):")
print(filtered_df[['Maths', 'Biology']].sort_values('Biology', ascending=False).head(10))

# Print summary statistics
print("\nSummary:")
print(f"Number of students with Biology >= 71: {len(filtered_df)}")

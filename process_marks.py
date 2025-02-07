import pandas as pd

# Read the extracted CSV file
df = pd.read_csv('extracted_tables.csv')

# Filter condition: Biology marks >= 71
filtered_df = df[df['Biology'] >= 71]

# Calculate total Maths marks
total_maths = filtered_df['Maths'].sum()

print(f"\nTotal Maths marks for students with Biology >= 71: {total_maths}")

print("\nFiltered student records (showing first 10):")
print(filtered_df[['Maths', 'Biology']].sort_values('Biology', ascending=False).head(10))

print("\nSummary:")
print(f"Number of students with Biology >= 71: {len(filtered_df)}")

# Additional verification
print("\nVerification:")
print("Biology marks distribution:")
print(filtered_df['Biology'].describe())

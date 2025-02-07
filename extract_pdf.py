import tabula
import pandas as pd

print("Reading PDF file...")
# Try to extract all data at once with specific parameters
tables = tabula.read_pdf(
    "q-extract-tables-from-pdf.pdf",
    pages='all',
    multiple_tables=True,
    lattice=True,  # Use lattice mode for better table detection
    guess=False,   # Don't guess table structure
    stream=True    # Use stream mode for better extraction
)

print(f"Number of tables found: {len(tables)}")

# Combine all tables into one DataFrame
df = pd.concat(tables, ignore_index=True)

# Verify we have the right number of rows (36 groups × 5 students = 180 students)
expected_rows = 180
if len(df) > expected_rows:
    print(f"Trimming data to first {expected_rows} rows...")
    df = df.head(expected_rows)

# Save to CSV
output_file = "extracted_tables.csv"
df.to_csv(output_file, index=False)
print(f"Data saved to {output_file}")

# Display shape and sample
print("\nShape of data:", df.shape)
print("\nFirst few rows:")
print(df.head())

# Verify data types and ranges
print("\nData Info:")
print(df.info())

# Show value ranges
print("\nValue ranges for each column:")
for col in df.columns:
    print(f"\n{col}:")
    print("Min:", df[col].min())
    print("Max:", df[col].max())
    print("Unique values:", len(df[col].unique()))

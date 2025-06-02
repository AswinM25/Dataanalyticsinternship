import pandas as pd


file_path = r"C:\Users\Aswin menon\Downloads\projectfolder\netflix_data.csv"
output_path = r"C:\Users\Aswin menon\Downloads\projectfolder\netflix_titles_cleaned.csv"
df = pd.read_csv(file_path)


df['country'].fillna('Unknown', inplace=True)
df['director'].fillna('Unknown', inplace=True)
df['date_added'].fillna('Unknown', inplace=True)


df_clean = df.drop_duplicates()
df_clean['rating'] = df_clean['rating'].astype(str).str.upper()
df_clean['country'] = df_clean['country'].str.title()
df_clean['type'] = df_clean['type'].str.lower()


df_clean['date_added'] = pd.to_datetime(df_clean['date_added'], errors='coerce')
df_clean.columns = [col.lower().replace(' ', '_') for col in df_clean.columns]
df_clean['release_year'] = df_clean['release_year'].astype(int)


output_path = 'netflix_titles_cleaned.csv'
df_clean.to_csv(output_path, index=False)


summary = {
    "Removed Duplicates": len(df) - len(df_clean),
    "Missing 'country' filled with": "Unknown",
    "Missing 'director' filled with": "Unknown",
    "Missing 'date_added' marked as": "Unknown",
    "Text fields standardized": ["rating", "country", "type"],
    "Date format standardized for": "date_added",
    "Column headers renamed to": "lowercase_with_underscores",
    "Data types adjusted for": "release_year (int)"
}

print("Data Cleaning Summary:")
for key, value in summary.items():
    print(f"- {key}: {value}")

print(f"\n Cleaned dataset saved as '{output_path}'")

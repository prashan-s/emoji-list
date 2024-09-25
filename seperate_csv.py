import pandas as pd

# Load the CSV file
df = pd.read_csv('si-filtered.csv')

# Condition to separate data (e.g., based on column 'Category')
categories = df['Page'].unique()

# Create a Pandas Excel writer to write into different sheets
with pd.ExcelWriter('output_file.xlsx', engine='xlsxwriter') as writer:
    for category in categories:
        # Filter data for each category and write to a new sheet
        df_category = df[df['Page'] == category]
        df_category.to_excel(writer, sheet_name=category, index=False)

print("CSV successfully split into Excel sheets!")

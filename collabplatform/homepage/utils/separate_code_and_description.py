import pandas as pd
import os

def separate_code_and_description(excel_file):
    df = pd.read_excel(excel_file)
    
    separated_data = []
    
    for index, row in df.iterrows():
        code = str(row.iloc[0]).strip()  # Accessing by position using iloc
        description = str(row.iloc[1]).strip()  # Accessing by position using iloc
        
        separated_data.append((code, description))
    
    return separated_data

# Specify the file path to the Excel file
excel_file = os.path.join("C:\\", "Users", "lukus", "Downloads", "Platform", "collabplatform", "homepage", "files", "Non-contracted.xlsx")

separated_data = separate_code_and_description(excel_file)

# Print the separated code and description
for code, description in separated_data:
    print(f"{code}, {description}")

# Print the separated code and description
for code, description in separated_data:
    print(f"{code}, {description}")

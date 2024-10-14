import pandas as pd
import json

# Load the Excel file
excel_file_path = 'restaurants.xlsx'  # Replace with the path to your Excel file

# Read the Excel file
# If your Excel file contains multiple sheets, specify the sheet name or index
excel_data = pd.read_excel(excel_file_path, sheet_name=0)  # Replace '0' with sheet name if needed

# Convert Excel data to JSON format
json_data = excel_data.to_json(orient='records', indent=4)

# Write the JSON data to a file
json_file_path = 'restaurants.json'  # Replace with the desired output file path
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"Excel file '{excel_file_path}' has been successfully converted to JSON and saved as '{json_file_path}'.")
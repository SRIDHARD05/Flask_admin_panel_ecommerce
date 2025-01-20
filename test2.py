from src.Reports import Reports
import json

file_path = 'sample.json'
try:
    with open(file_path, 'r') as file:
        data = json.load(file)  
        reports = Reports(data)
        print(reports.get_data())
        

except FileNotFoundError:
    print(f"File not found: {file_path}")
except json.JSONDecodeError:
    print("Error decoding JSON file")
except Exception as e:
    print(f"An error occurred: {str(e)}")



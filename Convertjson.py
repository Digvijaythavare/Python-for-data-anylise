import csv ,json

with open('data.csv') as csv_file:
    csv_reader = list(csv.DictReader(csv_file))

with open('data.json', 'w') as json_file:
    json.dump(csv_reader, json_file, indent=4)

print("CSV file has been converted to JSON format and saved as 'data.json'.")    

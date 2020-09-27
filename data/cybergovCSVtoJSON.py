import csv, json
#Variable CSV File
csvFilePath = "cyber_gov_au.csv" 
#Variable JSON output
jsonFilePath = "cybergov_output.json"

# Read CSV , Add data to dictionary
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        Threat_date = csvRow["Threat_date"]
        data[Threat_date] = csvRow
        
     
        
# Write data to JSON file
with open(jsonFilePath, "w") as jsonFile: 
    jsonFile.write(json.dumps(data, indent =4))

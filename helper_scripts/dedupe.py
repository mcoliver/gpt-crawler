import json

# Your input file
input_file="FILE.JSON"

# Load the original JSON file
with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)


# Create a dictionary to store unique entries based on the "url" field
unique_entries = {}

# Iterate through the original data and update the dictionary
for entry in data:
    url = entry.get("url")
    if url not in unique_entries:
        unique_entries[url] = entry

# Convert the dictionary values back to a list
deduplicated_data = list(unique_entries.values())

# Write the deduplicated data back to the file
with open('deduplicated_file.json', 'w', encoding='utf-8') as file:
    json.dump(deduplicated_data, file, ensure_ascii=False, indent=2)
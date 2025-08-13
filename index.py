import json

# Load data from the JSON file
with open('oscar_age_gender.json', 'r') as json_file:
    data = json.load(json_file)

# Extract unique years from the JSON data
years = sorted(set(item['Year'] for item in data))  # Set to avoid duplicates and sorted

# Write to index.html
with open("index.html", "w") as f:
    f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
    f.write('<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>Index Page</title>\n</head>\n<body>\n')
    f.write('<h1>Index of Oscar Years</h1>\n<ul>\n')

    # Loop through the years and generate list items with links
    for year in years:
        f.write(f'    <li><a href="/Years/{year}/{year}.html">{year}</a></li>\n')

    f.write('</ul>\n</body>\n</html>\n')

print("index.html generated successfully.")

import json

with open('oscar_age_gender.json', 'r') as json_file:
    data = json.load(json_file)

names = sorted(set(item['Name'] for item in data))

with open("names_list.html", "w") as f:
    f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
    f.write('<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>Index of Oscar Actors and Actresses</title>\n</head>\n<body>\n')
    f.write('<h1>Index of Oscar Actors and Actresses</h1>\n<ul>\n')

    for name in names:
        clean_name = name.replace(" ", "_")
        f.write(f'    <li><a href="/Actors_names/{clean_name}.html">{name}</a></li>\n')

    f.write('</ul>\n</body>\n</html>\n')

print("names_list.html generated successfully.")

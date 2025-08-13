import json
import os


with open('oscar_age_gender.json', 'r') as json_file:
    data = json.load(json_file)


actors_movies = {}


for entry in data:
    name = entry['Name']
    year = entry['Year']
    movie = entry['Movie']


    clean_name = name.replace(" ", "_")


    if clean_name not in actors_movies:
        actors_movies[clean_name] = []
    actors_movies[clean_name].append((year, movie))

os.makedirs("Actors_names", exist_ok=True)

for actor, movies in actors_movies.items():
    actor_filename = os.path.join("Actors_names", f"{actor}.html")

    with open(actor_filename, "w") as f:
        f.write(f'<!DOCTYPE html>\n<html lang="en">\n<head>\n')
        f.write(f'<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        f.write(f'<title>{actor.replace("_", " ")}</title>\n</head>\n<body>\n')
        f.write(f'<h1>Movies and Years of {actor.replace("_", " ")}</h1>\n')
        f.write('<table border="1">\n')
        f.write('<tr><th>Year</th><th>Movie</th></tr>\n')

        for year, movie in sorted(movies):
            f.write(f'<tr><td>{year}</td><td>{movie}</td></tr>\n')

        f.write('</table>\n</body>\n</html>\n')

    print(f"Generated: {actor_filename}")


with open("index-names.html", "w") as f:
    f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
    f.write('<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>Index Page</title>\n</head>\n<body>\n')
    f.write('<h1>Index of Actors and Actresses</h1>\n<ul>\n')

    for actor in actors_movies:
        f.write(f'    <li><a href="Actors_names/{actor}.html">{actor.replace("_", " ")}</a></li>\n')

    f.write('</ul>\n</body>\n</html>\n')

print("index.html generated successfully.")

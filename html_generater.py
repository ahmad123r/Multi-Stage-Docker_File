import os
import json

def generate_html(year, data, output_folder):

    year_folder = os.path.join(output_folder, str(year))
    os.makedirs(year_folder)


    year_file = os.path.join(year_folder, f"{year}.html")
    with open(year_file, "w") as f:
        f.write(f"<html><head><title>Oscar Awards {year}</title></head><body>")
        f.write(f"<h1>Oscar Awards {year}</h1>")
        f.write("<h2>Movies and Actors</h2><ul>")

   
        for entry in data:
            if entry['Year'] == year:
                f.write(f"<li><b>{entry['Name']}</b> in <i>{entry['Movie']}</i> ({entry['Gender']})</li>")

        f.write("</ul></body></html>")


def generate_index_html(years, output_folder):
    index_file = os.path.join(output_folder, "index.html")
    with open(index_file, "w") as f:
        f.write("<html><head><title>Oscar Awards Index</title></head><body>")
        f.write("<h1>Oscar Awards Index</h1>")
        f.write("<h2>Links to Yearly Data:</h2><ul>")
     
        for year in years:
            f.write(f'<li><a href="{year}/{year}.html">Oscar Awards {year}</a></li>')

        f.write("</ul></body></html>")


def read_json_data(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    input_file = "oscar_age_gender.json"  
    output_folder = "Years"  

    
    data = read_json_data(input_file)

 
    years = sorted(set(entry['Year'] for entry in data))


    os.makedirs(output_folder, exist_ok=True)

    for year in years:
        generate_html(year, data, output_folder)

    generate_index_html(years, output_folder)

    print(f"HTML files generated in the '{output_folder}' folder.")


if __name__ == "__main__":
    main()

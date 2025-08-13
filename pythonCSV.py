import csv
import requests

def download_csv(url):
    try:
        response = requests.get(url)  
        response.raise_for_status()  
        return response.content.decode('utf-8-sig').splitlines()  
    except requests.RequestException as e:
        print(f"Error downloading CSV {url}: {e}")
        return []


def process_data(reader, gender):
    data = []
    for row in reader:
        try:
            cleaned_row = {key.strip(): value for key, value in row.items()}  
            cleaned_row['Gender'] = gender  
            data.append(cleaned_row)
        except KeyError:
            print(f"invalid: {row}")  
    return data


female_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/oscar_age_female.csv'
male_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/oscar_age_male.csv'


female_csv = download_csv(female_url)
male_csv = download_csv(male_url)


csv_params = {
    'quoting': csv.QUOTE_ALL,   
    'skipinitialspace': True    
}

female_reader = csv.DictReader(female_csv, **csv_params)
male_reader = csv.DictReader(male_csv, **csv_params)

combined_data = (
    process_data(female_reader, 'F') +  
    process_data(male_reader, 'M')      
)


sorted_data = sorted(combined_data, key=lambda x: int(x['Year'])) 


for idx, row in enumerate(sorted_data, 1):
    row['Index'] = str(idx)  

fieldnames = ['Index', 'Year', 'Age', 'Name', 'Movie', 'Gender']  

with open('oscar_age_gender.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  
    writer.writerows(sorted_data)  

print("oscar_age_gender.csv has been created.")

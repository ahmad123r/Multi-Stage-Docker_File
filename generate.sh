#!/bin/bash


FEMALE_URL="https://assets.harridev.com/interview/oscar_age_female.json"
MALE_URL="https://assets.harridev.com/interview/oscar_age_male.json"


FEMALE_FILE="oscar_age_female.json"
MALE_FILE="oscar_age_male.json"
OUTPUT_FILE="oscar_age_gender1.json"
FINAL_OUTPUT="oscar_age_gender.json"


wget -q --show-progress "$FEMALE_URL" -O "$FEMALE_FILE"
wget -q --show-progress "$MALE_URL" -O "$MALE_FILE"


if [[ ! -f "$FEMALE_FILE" || ! -f "$MALE_FILE" ]]; then
    echo "Error: One or both JSON files are missing!"
    exit 1
fi

echo "Merging both files..."


jq '[.[] | . + {"Gender": "F"}]' "$FEMALE_FILE" > Modified_female.json
jq '[.[] | . + {"Gender": "M"}]' "$MALE_FILE" > Modified_male.json


jq -s 'add | sort_by(.Year)' Modified_female.json Modified_male.json > "$OUTPUT_FILE"

jq 'to_entries | map(.value.Index = (.key + 1)) | map(.value)' "$OUTPUT_FILE" > "$FINAL_OUTPUT"


rm -f Modified_female.json Modified_male.json

echo "Processing complete! Output saved to $FINAL_OUTPUT"


# echo "Done!!"
sleep 1
python3 html_generater.py
 sleep 1
 python3 index.py

 sleep 1
python3 index-name.py
 sleep 1
python3 indexname.py
 sleep 1


mv Years generated_artifacts/
mv index.html generated_artifacts/
mv Actors_names generated_artifacts/
mv index-names.html generated_artifacts/
mv names_list.html generated_artifacts/
mv oscar_age_gender.json generated_artifacts/

# # python3 app.py
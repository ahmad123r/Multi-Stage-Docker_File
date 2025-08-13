
jq -s 'add | sort_by(.Year)' Modified_female.json Modified_male.json > "$OUTPUT_FILE"
the add word was missing so added it and python script for CSV are done 
generating names html and index for them are done
creating a multi-staging dockerfile to make the size less the first image for artifact and the other to run it 

for years index : http://localhost:8090/index.html
for names index :http://localhost:8090/names_list.html

import requests
import csv
import os

# Define the URL of the CSV file
url = "https://raw.githubusercontent.com/12v/boundary-mapper/main/output/condensed_postcode_to_constituency_mapping.csv"

# Send a GET request to the URL and get the content
response = requests.get(url)

# Decode the content to text
content = response.content.decode()

# Use the csv reader to read the content line by line
reader = csv.reader(content.splitlines())

# Skip the header
next(reader)

# For each line, get the postcode and the new_constituency_name
for row in reader:
    postcode, new_constituency_name = row

    # Remove whitespace from the postcode to use it as a filename
    filename = postcode.replace(" ", "")

    # Create a new text file in the 'docs' directory with the filename as the postcode
    with open(os.path.join('docs', f'{filename}.txt'), 'w') as f:
        # Write the new_constituency_name to the text file
        f.write(new_constituency_name)
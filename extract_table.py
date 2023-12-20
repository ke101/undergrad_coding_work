import requests
from bs4 import BeautifulSoup
import sys
import csv

# Step 1: Make a request to the webpage
url = sys.argv[1]
response = requests.get(url)
# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find and extract tables
tables = soup.find_all('table')

for i, table in enumerate(tables):
    # Generate a unique filename for each CSV
    filename = f'table_{i}.csv'

    # Open a CSV file for writing
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Extract rows and write to CSV
        for row in table.find_all('tr'):
            csvwriter.writerow([cell.text for cell in row.find_all(['th', 'td'])])
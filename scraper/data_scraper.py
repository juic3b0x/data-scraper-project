# data-scraper-project/scraper/data_scraper.py

import requests
from bs4 import BeautifulSoup
from database.db_manager import add_promo_codes

def scrape_promo_codes(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', {'id': 'promos'})  # Target the table with id 'promos'

    promo_codes = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        if len(columns) >= 3:  # Make sure there are enough columns
            code = columns[0].text.strip()
            promo = columns[2].text.strip()  # Adjust index for 'Promo' column as necessary
            promo_codes.append((code, promo))
    
    return promo_codes

def save_promo_codes_to_database(promo_codes):
    add_promo_codes(promo_codes)

if __name__ == "__main__":
    url = "https://tld-list.com/promo-codes"
    promo_codes = scrape_promo_codes(url)
    save_promo_codes_to_database(promo_codes)

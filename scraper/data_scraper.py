# data-scraper-project/scraper/data_scraper.py

import requests
from bs4 import BeautifulSoup
from database.db_manager import add_promo_codes

def scrape_promo_codes(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table')  # Assuming there's only one table on the page

    promo_codes = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        code = columns[0].text.strip()
        promo = columns[1].text.strip()
        promo_codes.append((code, promo))
    
    return promo_codes

def save_promo_codes_to_database(promo_codes):
    add_promo_codes(promo_codes)

if __name__ == "__main__":
    url = "https://tld-list.com/promo-codes"
    promo_codes = scrape_promo_codes(url)
    save_promo_codes_to_database(promo_codes)

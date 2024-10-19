import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
import time
from random import randint
import sys
print(sys.executable)

#for commit
def scrape_country_data():
    url = "https://data.worldbank.org/country"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    session = requests.Session()
    session.headers.update(headers)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    countries_data = {}

    
    country_links = soup.select("section.nav-item ul li a")  
    
    for link in country_links:
        country_name = link.text.strip()
        relative_url = link['href']
        country_url = urljoin(url, relative_url)
        country_code = country_url.split('locations=')[-1]  

        country_response = requests.get(country_url)
        country_soup = BeautifulSoup(country_response.content, "html.parser")

        
        
        indicator_section = country_soup.select_one('div.indicator-item[id="0"]')

        if indicator_section:
            
            indicator_items = indicator_section.select('div.indicator-item__wrapper')
            
            indicators = []
            
            
            for item in sorted(indicator_items, key=lambda x: int(x['style'].split('z-index:')[-1].strip().rstrip(';')), reverse=True):
                
                title_tag = item.select_one('div.indicator-item__title a')
                data_info_tag = item.select_one('div.indicator-item__data-info span') or \
                                item.select_one('p.indicator-item__data-info-empty span')

                
                if title_tag and data_info_tag:
                    indicator_title = title_tag.text.strip()
                    indicator_data = data_info_tag.text.strip()

                    indicators.append({
                        "title": indicator_title,
                        "data": indicator_data
                    })

            
            countries_data[country_name] = {
                # "name": country_name,
                "url": country_url,
                "indicators": indicators
            }

            time.sleep(randint(1, 8))

        

    
    with open('data/countries_data.json', 'w') as f:
        json.dump(countries_data, f, indent=4)
    
    print(f"Total number of countries scraped: {len(countries_data)}")

if __name__ == "__main__":
    scrape_country_data()

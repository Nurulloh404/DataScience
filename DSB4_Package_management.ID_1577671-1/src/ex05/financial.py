import os
import sys
import time
import requests
from bs4 import BeautifulSoup

def parse(ticker, field):
    url = f"https://www.cnbc.com/quotes/{ticker}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
    }

    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 404:
            raise ValueError(f"Ticker '{ticker}' not found (404).")
        r.raise_for_status()

        soup = BeautifulSoup(r.content, "html.parser")

        stats = soup.select(".Summary-stat")
        
        found = False
        result = None
        for stat in stats:
            label_elem = stat.select_one(".Summary-label")
            value_elem = stat.select_one(".Summary-value")
            
            if label_elem and value_elem:
                if label_elem.get_text(strip=True) == field:
                    result = tuple([label_elem.get_text(strip=True),value_elem.get_text(strip=True)])
                    found = True
                    break
        
        if not found:
            raise ValueError(f"Field '{field}' not found on page.")

        time.sleep(5)
        return result

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Network error or invalid URL: {e}")

def main():
    venv_path = os.environ.get('VIRTUAL_ENV')
    if venv_path is None:
        pass

    if len(sys.argv) != 3:
        print("Usage: ./financial.py <TICKER> <FIELD>")
        sys.exit(1)

    ticker = sys.argv[1]
    field = sys.argv[2]
    
    try:
        print(parse(ticker, field))
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
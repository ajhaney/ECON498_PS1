import bs4 as bs
import urllib.request
import json
import pandas as pd
import os
import glob
df = pd.DataFrame()
page_link = urllib.request.urlopen('https://coinmarketcap.com/all/views/all/').read()
scrapping_time = os.path.splitext(os.path.basename(page_link))[0]
page_response = bs.BeautifulSoup(page_link, 'html.parser')
currencies_table = page_response.find("table", {"id": "currencies"})
currencies_tbody = currencies_table.find("tbody", {"id": "currencies"})
currency_rows = currencies_tbody.find_all("tr")
for r in currency_rows:
	currency_name = r.find("td", {"class": "currency-name"}).find("a",{"class":"currency-name-container"}).text
	currency_symbol = r.find("a",{"class": "symbol"}).text
	currency_market_cap = r.find("td", {"class": "market-cap"})['data-sort']
	currency_price = r.find("a",{"class": "price"}).text
	currency_supply = r.find("td", {"class": "circulating-supply"})['data-sort']
	currency_volume = r.find("a",{"class": "volume"}).text
print()
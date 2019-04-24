# ECON498_PS1

REQUEST
for i in range(2133):
  Change the number in order to increase or decrease the number of cryptocurrencies to scrape
current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	print(str(i) + ": " + current_time_stamp)
    Takes current time stamp of all cryptocurrencies requested and prints it in order
time.sleep(30)
  Change the numbers to increase or decrease the amount of time in between scrapping the cryptocurrencies



coinmarketcap_Parse

This is the code straight from the lecture on scraping coinmarketcap, however this code was buggy on my laptop so I did a couple things to try to fix the error in the next 2 files
The error I kept receiving was File "coinmarketcap_parse.py", line 17, in <module> soup = BeautifulSoup(f.read(), 'html.parser') File "C:\Users\.....,line 23, in decode return codecs.charmap_decode(input,self.errors,decoding_table)[0]


coin_market_cap

This was one of my attempts at fixing the error, however it remained the same

coin_market

This was my last attempt to fix the error, I made minimal changes to the original code in order to try to isolate the problem thus solving the issue easier, but after a few changes to line 17 and 23 of the original code, I could not find the error. Line 17 kept giving errors and deleting line 23 simply pushed the error to line 24 (line 22 in this script).


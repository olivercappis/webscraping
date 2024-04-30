from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = 'https://www.webull.com/quote/crypto'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')



crypto_data = soup.findAll('div', attrs={'class': 'table-cell'})


name_counter = 0
counter = 2
for x in range(5):
    name_data = soup.findAll('p', attrs={'class': 'tit bold'})
    name = name_data[name_counter].text
    current_price = float(crypto_data[counter ].text.replace(',',''))
    change = float(crypto_data[counter + 1].text.strip('%').replace(',',''))
    prev_price = round(current_price / (1 + (change/100)))
    



    print()
    print()
    print('Coin name:', name)
    print('Current Price:', current_price)
    print('Change:', change)
    print('Previous Price:', prev_price)
    print()
    print()

    counter += 10
    name_counter += 1


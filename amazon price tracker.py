import requests, time
from bs4 import BeautifulSoup
url=input("Enter url: ").strip();
headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}


res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
price = soup.select('#priceblock_ourprice')[0].getText()
print(price)
import time
time.sleep(3);


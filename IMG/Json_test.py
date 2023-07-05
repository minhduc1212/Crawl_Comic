from bs4 import BeautifulSoup
import cloudscraper
import os
from time import sleep
from fake_useragent import UserAgent
from urllib.parse import urljoin
import re
import json

scraper = cloudscraper.create_scraper()
ua = UserAgent()
headers =   {
                'User-Agent': ua.random,
                'Referer': 'https://www.nettruyenmax.com/'
            }

url=input("Link Truyện: ", )

response=scraper.get(url, headers=headers)
soup=BeautifulSoup(response.text, "html.parser") 

comic_name=soup.find('h1', {'class':'title-detail'}).text

sleep(0.5)
with open('{}.json'.format(comic_name), 'a', encoding='utf-8') as f:
        f.write("sssss")

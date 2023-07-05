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

path = input("Vị Trí Tải Truyện: ",)
if not os.path.exists(os.path.join(path, comic_name)):
    os.makedirs(path)

with open('{}.json'.format(comic_name), 'r', encoding='utf-8') as f:
    data = json.load(f)

for chap in data:
    chap_imgs = chap['image_links']
    chap_name = chap['chapter_name']

    chap_path = os.path.join(path, chap_name)
    if not os.path.exists(chap_path):
        os.makedirs(chap_path)
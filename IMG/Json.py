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

areas=soup.find_all('div', {'class':'col-xs-5 chapter'})

sleep(0.5)

chap_links = []
chap_names = []
data = []

for area in areas:
    link=area.find('a')
    chap_links.append(link['href'])

    chap_name=area.get_text().strip()
    chap_name = re.sub(r'[\\/:*?"<>|]', ' ', chap_name)
    chap_names.append(chap_name)
    
    data_one = {
        "chapter_name": chap_name,
        "image_links": []
            }

    for chap_link in chap_links:
        chap_response=scraper.get(chap_link, headers=headers)
        chap_soup=BeautifulSoup(chap_response.text, "html.parser")
        chap_imgs_div=chap_soup.find('div', {'class':'reading-detail box_doc'})
        chap_imgs=chap_imgs_div.find_all('img')

        sleep(0.5)
        
        data_one["image_links"].extend([img.get('src') for img in chap_imgs])      
    data.append(data_one)

with open('{}.json'.format(comic_name), 'a', encoding='utf-8') as f:
    json.dump(data_one,f)


    

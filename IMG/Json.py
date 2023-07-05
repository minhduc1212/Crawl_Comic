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
                'Referer': 'https://www.nettruyenplus.com/'
            }

url=input("Link Truyện: ", )

response=scraper.get(url, headers=headers)
soup=BeautifulSoup(response.text, "html.parser") 

areas=soup.find_all('div', {'class':'col-xs-5 chapter'})

sleep(1)

chap_links = []

for area in areas:
    link=area.find('a')
    chap_links.append(link['href'])

    chap_names = []
    chap_name=area.get_text().strip()
    chap_name = re.sub(r'[\\/:*?"<>|]', ' ', chap_name)
    chap_names.append(chap_name)

    data = {
        "chapter_name": chap_name,
        "image_links": []
            }
    
    for chap_link in chap_links:
        chap_response=scraper.get(chap_link, headers=headers)
        chap_soup=BeautifulSoup(chap_response.text, "html.parser")
        chap_imgs_div=chap_soup.find('div', {'class':'reading-detail box_doc'})
        chap_imgs=chap_imgs_div.find_all('img')

        sleep(0.5)

        data["image_links"].extend([img['src'] for img in chap_imgs])

    with open('data.json', 'a', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
        f.write('\n')
    

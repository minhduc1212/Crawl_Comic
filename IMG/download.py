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
if not os.path.exists(path):
    os.makedirs(path)
if not os.path.exists(os.path.join(path, comic_name)):
    os.makedirs(os.path.join(path, comic_name))

with open('{}.json'.format(comic_name), 'r') as f:
    data = json.load(f)

for record in data:
    chap_imgs = record['image_links']
    chap_name = record['chapter_name']

    chap_path = os.path.join(os.path.join(path, comic_name), chap_name)
    if not os.path.exists(chap_path):
        os.makedirs(chap_path)

    for img_link in chap_imgs:
                
        img_link_fix=urljoin(url, img_link)

        response_img=scraper.get(img_link_fix, headers=headers)

        filename = img_link_fix.split('/')[-1].split('?')[0] 
   
        with open(os.path.join(chap_path, filename), 'wb') as f:
            f.write(response_img.content)
        sleep(0.5)
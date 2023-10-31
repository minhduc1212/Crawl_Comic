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
                'Referer': 'https://www.nettruyenus.com/'
            }

url=input("Link Truyện: ", )
path=input("Đường dẫn lưu: ", )
if not os.path.exists(path):
    os.makedirs(path)

response=scraper.get(url, headers=headers)
soup=BeautifulSoup(response.text, "html.parser") 

comic_name=soup.find('h1', {'class':'title-detail'}).text
comic_name = re.sub(r'[\\/:*?"<>|]', ' ', comic_name)

areas=soup.find_all('div', {'class':'col-xs-5 chapter'})


data = []
for i, area in enumerate(areas):
    link=area.find('a')

    chap_name=area.get_text().strip()
    chap_name = re.sub(r'[\\/:*?"<>|]', ' ', chap_name)
    chap_names = []
    chap_names.append(chap_name)

    data_one = {
        "chapter_name": chap_name,
        "image_links": []
            }

    chap_links = []
    chap_links.append(link['href'])
    for chap_link in chap_links:
        chap_response=scraper.get(chap_link, headers=headers)
        chap_soup=BeautifulSoup(chap_response.text, "html.parser")
        chap_imgs_div=chap_soup.find('div', {'class':'reading-detail box_doc'})
        chap_imgs=chap_imgs_div.find_all('img')

        sleep(0.5)
            
        data_one["image_links"].extend([img.get('src') for img in chap_imgs])     
    data.append(data_one)
with open('{}/{}.json'.format(path, comic_name), 'w', encoding='utf-8') as f:
    json.dump(data,f, ensure_ascii=False)


        



    

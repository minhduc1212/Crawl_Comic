from bs4 import BeautifulSoup
import cloudscraper
import os
from time import sleep
from fake_useragent import UserAgent
from urllib.parse import urljoin
import re
import json

scraper = cloudscraper.create_scraper()
with open ('all_comics_links_list.json', 'r', encoding='utf-8') as f:
    comics = json.load(f)
while True:
    ua = UserAgent()
    headers =   {
                    'User-Agent': ua.random,
                    'Referer': 'https://www.nettruyenus.com/'
                }

    count = 0
    for comic in comics :

        comic_name=comic['comic_name']
        comic_name = re.sub(r'[\\/:*?"<>|]', ' ', comic_name)

        comic_link=comic['comic_link']

        file_path = os.path.join('E:/LT/Crawl (Python)/Data', f'{comic_name}.json')
        if os.path.exists(file_path):
            print(f'{comic_name} đã được lưu trữ, bỏ qua') 
            continue

        response=scraper.get(comic_link, headers=headers)
        soup=BeautifulSoup(response.text, "html.parser") 
        areas=soup.find_all('div', {'class':'col-xs-5 chapter'})

        sleep(0.5)

        with open(file_path, 'a', encoding='utf-8') as f:
            for area in areas:
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
                json.dump(data_one,f)
                f.write('\n') 

                print("Đã lấy xong dữ liệu của {} truyện {}".format(chap_name, comic_name))
        count += 1
        if count == len(comics):
            break
    sleep(3600)

        

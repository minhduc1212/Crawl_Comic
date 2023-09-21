from bs4 import BeautifulSoup
import cloudscraper
import os
from time import sleep
from fake_useragent import UserAgent
from urllib.parse import urljoin
import re
import json
import datetime

while True:
    scraper = cloudscraper.create_scraper()
    ua = UserAgent()
    headers =   {
                    'User-Agent': ua.random,
                    'Referer': 'https://www.nettruyenus.com/'
                }

    now = datetime.datetime.now()
    formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")

    response=scraper.get('https://www.nettruyenus.com/', headers=headers)
    soup=BeautifulSoup(response.text, "html.parser") 

    comic_links = [comic['href'] for comic in soup.find_all('a', {'class': 'jtip'})]

    for comic_link in comic_links:
        comic_link_response=scraper.get(comic_link, headers=headers)

        comic_soup=BeautifulSoup(comic_link_response.text, "html.parser") 
        comic_name=comic_soup.find('h1', {'class':'title-detail'}).text
        comic_name = re.sub(r'[\\/:*?"<>|]', ' ', comic_name)

        areas=comic_soup.find_all('div', {'class':'col-xs-5 chapter'})

        sleep(0.5)

        comic_file = 'E:/LT/Crawl (Python)/Data/{}.json'.format(comic_name)

        if os.path.exists(comic_file):
            chap_dict = {}
            for area in areas:
                link = area.find('a')
                chap_link=link['href']

                chap_name = area.get_text().strip()
                chap_name = re.sub(r'[\\/:*?"<>|]', ' ', chap_name)

                chap_dict[chap_name] = chap_link

            with open(comic_file, 'r', encoding='utf-8') as f:
                datas = json.load(f)
            
            chapter_names=[]
            for data in datas:
                chapter_name=data['chapter_name']
                chapter_names.append(chapter_name)

            for chap_name, chap_link in chap_dict.items():
                if chap_name not in chapter_names:

                    data_one = {
                    "chapter_name": chap_name,
                    "image_links": []
                                }

                    chap_response=scraper.get(chap_link, headers=headers)
                    chap_soup=BeautifulSoup(chap_response.text, "html.parser")
                    chap_imgs_div=chap_soup.find('div', {'class':'reading-detail box_doc'})
                    chap_imgs=chap_imgs_div.find_all('img') 

                    data_one["image_links"].extend([img.get('src') for img in chap_imgs]) 

                    datas.append(data_one)

            with open(comic_file, 'w', encoding='utf-8') as f:
                json.dump(datas, f, ensure_ascii=False)

            with open('history.txt', 'a', encoding='utf-8') as f:
                f.write(formatted_time + " Update truyện " + comic_name + "\n")
            print(formatted_time, " Update truyện ", comic_name)

        else:
            with open('E:/LT/Crawl (Python)/Data/{}.json'.format(comic_name), 'w', encoding='utf-8') as f:
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
                    json.dump(data_one,f, ensure_ascii=False)
                    f.write('\n') 

                    print("Đã lấy xong dữ liệu của {}".format(chap_name))
            
            data = []

            with open('E:/LT/Crawl (Python)/Data/{}.json'.format(comic_name), 'r', encoding='utf-8') as f:
                for line in f:
                    data_one = json.loads(line)
                    data.append(data_one)

            with open('E:/LT/Crawl (Python)/Data/{}.json'.format(comic_name), 'w', encoding='utf-8') as s:
                json.dump(data,s, ensure_ascii=False)
            
            with open('history.txt', 'a', encoding='utf-8') as f:
                f.write(str(formatted_time + " Update " + comic_name + "\n"))

            print(formatted_time, " Update ", comic_name)
    sleep(1800)
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

with open('{}.json'.format(comic_name), 'r', encoding='utf-8') as f:
    data = [json.loads(line) for line in f]

visited_links = set()

for chap in data:
    chap_imgs = chap['image_links']
    chap_name = chap['chapter_name']

    chap_path = os.path.join(os.path.join(path, comic_name), chap_name)
    if not os.path.exists(chap_path):
        os.makedirs(chap_path)

    for idx, img_link in enumerate(chap_imgs, 1):
        
        img_link_fix=urljoin(url, img_link)

        # Kiểm tra xem link đã được tải chưa
        if img_link_fix in visited_links:
            print(f"Link {img_link_fix} has already been visited")
            continue

        # Tải ảnh và lưu vào thư mục tương ứng
        response_img=scraper.get(img_link_fix, headers=headers)

        filename = img_link_fix.split('/')[-1].split('?')[0] 
        
        with open(os.path.join(chap_path, filename), 'wb') as f:
            f.write(response_img.content)
        print(f"{idx}/{len(chap_imgs)} ({idx/len(chap_imgs)*100:.2f}%)")

        visited_links.add(img_link_fix)  # Cập nhật danh sách các link đã được tải
        sleep(0.5)
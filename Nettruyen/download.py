from bs4 import BeautifulSoup
import cloudscraper
import os
import time
from fake_useragent import UserAgent
from urllib.parse import urljoin    
import re
import json
import threading

def download():
    scraper = cloudscraper.create_scraper()
    ua = UserAgent()
    headers =   {
                    'User-Agent': ua.random,
                    'Referer': 'https://www.nettruyenus.com/'
                }

    url=input("link Truyện : ", )

    response=scraper.get(url, headers=headers)
    soup=BeautifulSoup(response.text, "html.parser") 
        
    comic_name=soup.find('h1', {'class':'title-detail'}).text  
    comic_name = re.sub(r'[\/:*?"<>|]', ' ', comic_name)

    time.sleep(0.5)

    path = input("Vị Trí Tải Truyện: ",)

    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(os.path.join(path, comic_name)):
        os.makedirs(os.path.join(path, comic_name))

    with open('E:/LT/Crawl (Python)/Data/{}.json'.format(comic_name), 'r', encoding='utf-8') as f:
        data = json.load(f)

    def download_images(record):
        chap_imgs = record['image_links']
        chap_name = record['chapter_name']
        chap_name = re.sub(r'[\/:*?"<>|]', ' ', chap_name)
        chap_name = " ".join(chap_name.split())

        chap_path = os.path.join(os.path.join(path, comic_name), chap_name)
        if not os.path.exists(chap_path):
            os.makedirs(chap_path)

        img_count = 1
        for img_link in chap_imgs:
            img_link_fix = urljoin(url, img_link)

            response_img = scraper.get(img_link_fix, headers=headers)

            filename = f'{img_count:03}.jpg'

            with open(os.path.join(chap_path, filename), 'wb') as f:
                f.write(response_img.content)
            img_count += 1

        print("Đã tải xong", chap_name)
        time.sleep(0.5)

    threads = []
    for record in data:
        thread = threading.Thread(target=download_images, args=(record,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
start_time=time.time()

download_thread=threading.Thread(target=download)
download_thread.start()
download_thread.join()

end_time = time.time()
print(f"Thời gian load: {end_time - start_time} giây")
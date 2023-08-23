from flask import Flask, request, render_template, jsonify
from bs4 import BeautifulSoup
import cloudscraper
import os
from time import sleep
from fake_useragent import UserAgent
from urllib.parse import urljoin    
import re
import json
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def download():
    scraper = cloudscraper.create_scraper()
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Referer': 'https://www.nettruyenmax.com/'
                }

    url = request.form.get('url')
    path = request.form.get('path')

    response = scraper.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser") 
        
    comic_name = soup.find('h1', {'class':'title-detail'}).text  
    comic_name = re.sub(r'[\/:*?"<>|]', ' ', comic_name)

    sleep(0.5)

    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(os.path.join(path, comic_name)):
        os.makedirs(os.path.join(path, comic_name))

    with open('E:/LT/Crawl (Python)/Data/{}.json'.format(comic_name), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for record in data:
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
        sleep(0.5)
        
@app.route('/download', methods=['POST'])
def download_thread():
    download = threading.Thread(target=download)
    download.start()

    return render_template('download.html')

if __name__ == '__main__':
    app.run(port=8081)
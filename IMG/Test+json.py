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

url="https://www.nettruyenmax.com/truyen-tranh/dai-phung-da-canh-nhan-556590"
response=scraper.get(url, headers=headers)
soup=BeautifulSoup(response.text, "html.parser") 
areas=soup.find_all('div', {'class':'col-xs-5 chapter'})

sleep(1)

path = 'E:\T\TTr/Đại Phụng Đả Canh Nhân'
if not os.path.exists(path):
    os.makedirs(path)

chap_links = []
for i in range(190,192):
    area = areas[i]
    link=area.find('a')
    chap_links.append(link['href'])

    chap_names = []
    chap_name=area.get_text().strip()
    chap_name = re.sub(r'[\\/:*?"<>|]', ' ', chap_name)
    chap_names.append(chap_name)

    # Lưu trữ dữ liệu về ảnh vào dictionary
    data = {
        "chapter_name": chap_name,
        "image_links": []
    }

    chap_path = os.path.join(path, chap_name)

    if not os.path.exists(chap_path):
        os.makedirs(chap_path)
        sleep(0.5)

    for chap_link in chap_links:
        chap_response=scraper.get(chap_link, headers=headers)
        chap_soup=BeautifulSoup(chap_response.text, "html.parser")
        chap_imgs_div=chap_soup.find('div', {'class':'reading-detail box_doc'})
        chap_imgs=chap_imgs_div.find_all('img')
        sleep(0.5)

        # Thêm đường dẫn ảnh vào dictionary
        data["image_links"].extend([img['src'] for img in chap_imgs])

    # Thêm dữ liệu vào file JSON
    with open('data.json', 'a', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
        f.write('\n')

# Đọc dữ liệu từ file JSON
with open('data.json', 'r', encoding='utf-8') as f:
    data = [json.loads(line) for line in f]

visited_links = set()   # Khởi tạo danh sách các link đã được tải

for chap in data:
    chap_name = chap['chapter_name']
    chap_imgs = chap['image_links']
    chap_path = os.path.join(path, chap_name)

    if not os.path.exists(chap_path):
        os.makedirs(chap_path)
        sleep(0.5)

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
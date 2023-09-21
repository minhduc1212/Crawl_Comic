from bs4 import BeautifulSoup
import cloudscraper
import os
from time import sleep
from fake_useragent import UserAgent
from urllib.parse import urljoin
import re

scraper = cloudscraper.create_scraper()
ua = UserAgent()
headers =   {
                'User-Agent': ua.random,
                'Referer': 'https://www.nettruyenus.com/'
            }

url="https://www.nettruyenus.com/truyen-tranh/dai-phung-da-canh-nhan-556590"
response=scraper.get(url, headers=headers)
soup=BeautifulSoup(response.text, "html.parser") 
areas=soup.find_all('div', {'class':'col-xs-5 chapter'})

sleep(0.5)

path = 'D:\T (Part D)\Đại Phụng Đả Canh Nhân'
if not os.path.exists(path):
    os.makedirs(path)

for i in range(1):
    chap_links = []
    area = areas[i]
    link=area.find('a')
    chap_links.append(link['href'])

    chap_names = []
    chap_name=area.get_text().strip()
    chap_name = re.sub(r'[\\/:*?"<>|]', ' ', chap_name)
    chap_names.append(chap_name)
    chap_path = os.path.join(path, chap_name)

    if not os.path.exists(chap_path):
        os.makedirs(chap_path)
        sleep(0.5)

    for chap_link in chap_links:
        chap_response=scraper.get(link, headers=headers)
        chap_soup=BeautifulSoup(chap_response.text, "html.parser")
        chap_imgs_div=chap_soup.find('div', {'class':'reading-detail box_doc'})
        chap_imgs=chap_imgs_div.find_all('img')
        sleep(0.5)

    for idx, img in enumerate(chap_imgs, 1):
        img_link = img['src']
        img_link_fix=urljoin(url, img_link)
        response_img=scraper.get(img_link_fix, headers=headers)

        filename = img_link_fix.split('/')[-1].split('?')[0] 
        with open('D:\T (Part D)\Đại Phụng Đả Canh Nhân\{}\{}'.format(chap_name, filename), 'wb') as f:
            f.write(response_img.content)
        sleep(0.5)
        print(f"{idx}/{len(chap_imgs)} ({idx/len(chap_imgs)*100:.2f}%)")


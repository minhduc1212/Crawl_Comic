import requests
import cloudscraper
from bs4 import BeautifulSoup
import json
import os
from time import sleep
from fake_useragent import UserAgent
from urllib.parse import urljoin
import re

scraper = cloudscraper.create_scraper()
ua = UserAgent()
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://www.nettruyenmax.com/'
}
url = "https://www.nettruyenmax.com/tim-truyen-nang-cao?genres=&notgenres=&gender=-1&status=-1&minchapter=1&sort=15&page={}"

with open('all_comics_links.json', 'w', encoding='utf-8') as f:
    for i in range(1, 513):
        # Tạo đường dẫn của trang tiếp theo
        next_url = url.format(i)
        response = scraper.get(next_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        comic_names = [comic.get_text() for comic in soup.find_all('a', {'class': 'jtip'})] #Đây là một cách làm nhanh, cách làm khác là tạo ra 2 list comic_names và comic_links rồi dùng append
        comic_links = [comic['href'] for comic in soup.find_all('a', {'class': 'jtip'})]
        for comic_name, comic_link in zip(comic_names, comic_links):
            comic = {
                "comic_name": comic_name,
                "comic_link": comic_link
                    }
            json.dump(comic, f, ensure_ascii=False)
            f.write('\n')
        print("Đã lấy xong dữ liệu của trang {}".format(i))

from bs4 import BeautifulSoup
"""
html = '''
<div class="test">First div</div>
<div class="test">Second div</div>
'''

soup = BeautifulSoup(html, 'html.parser')
divs = soup.find_all('div', {'class': 'test'})
print(divs)
for div in divs:
    print(div.text)
"""
import requests
import os

# URL của truyện
url = 'https://truyenfull.vn/linh-vu-thien-ha/'

# Thực hiện yêu cầu HTTP và phân tích cú pháp HTML của trang đầu tiên
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tìm số lượng chương của truyện
chapter_list = soup.find_all('div', {'class': 'col-xs-12 col-sm-6 col-md-6'})
chapters_links = []
for chapter in chapter_list:
    chapter_links = chapter.find_all('a')    
    for link in chapter_links:
        chapters_links.append(link['href'])#truy cập vào href trong thẻ a
for one_link in chapters_links:
    response_link = requests.get(one_link)
    soup1 = BeautifulSoup(response_link.text, 'html.parser')
    text=soup1.get_text()
    text1=str(text)
    with open("1.txt", 'a',  encoding='utf-8') as s:
        s.write(text1)
                
                





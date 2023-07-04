import requests
from bs4 import BeautifulSoup


# Tải nội dung của trang web
url = 'https://truyenfull.vn/linh-vu-thien-ha/chuong-1/'
url_f='https://truyenfull.vn/linh-vu-thien-ha/'
response = requests.get(url)
response_f=requests.get(url_f)

# Phân tích cú pháp HTML của trang web
soup = BeautifulSoup(response.text, 'html.parser')
div = soup.find('div', {'id': 'chapter-c', 'class': 'chapter-c', 'itemprop': 'articleBody'})
text=div.get_text(separator='\n')

soup_f=BeautifulSoup(response_f.text, 'html.parser')
a=soup_f.find('a', {'title':'Linh Vũ Thiên Hạ - Chương 1: Nhân phẩm có vấn đề (1)'})
text_f=a.get_text()

path = "E:/LT/Crawl (Python)/1.txt"
with open(path, 'w', encoding="utf-8") as a:
    a.write(text_f + '\n')
    a.write(text)
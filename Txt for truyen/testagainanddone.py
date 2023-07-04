import requests
from bs4 import BeautifulSoup

url = 'https://truyenfull.vn/linh-vu-thien-ha/chuong-1/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Tìm thẻ div chứa nội dung truyện
chapter_div = soup.find('div', {'class': 'chapter-c', 'id': 'chapter-c', 'itemprop': 'articleBody'})

# Lấy ra nội dung của thẻ div
chapter_content = chapter_div.get_text(separator='\n')

# In ra nội dung của đoạn truyện
print(chapter_content)
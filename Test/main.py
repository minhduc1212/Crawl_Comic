import requests
from bs4 import BeautifulSoup

# Tải nội dung của trang web
url = 'https://truyenfull.vn/linh-vu-thien-ha/'
response = requests.get(url)

# Phân tích cú pháp HTML của trang web
soup = BeautifulSoup(response.text, 'html.parser')

# Lấy tất cả các liên kết trên trang web
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

# In ra các liên kết
print(links)

#Kết hợp với in links ra file
with open('links.xlsx', 'w') as f:
    links_str = '\n'.join(links)  
    f.write(links_str)    

#Đưa toàn bộ code của web ra file
with open('1.html', 'w', encoding='utf-8') as s:
    soup_str = str(soup)
    s.write(soup_str)
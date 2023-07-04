import requests
from bs4 import BeautifulSoup

# Tải nội dung của trang web
url = 'http://banlong.us/threads/hua-tien-chi-thuyet-mong-than-full.9229/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Lấy tất cả các phần tử div có class 'SpoilerTarget bbCodeSpoilerText'
divs = soup.find_all('div', {'class':'SpoilerTarget bbCodeSpoilerText'})

# Lưu trữ nội dung của mỗi phần tử div vào một tệp văn bản khác nhau
for i, div in enumerate(divs, 1):
    content = div.get_text()
    name = f"chapter_{i}.txt" # Tạo tên tệp văn bản mới
    with open(name, 'w', encoding="utf-8") as f:
        f.write(content)

    
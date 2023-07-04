import requests
from bs4 import BeautifulSoup

# URL của trang web chứa thẻ div cần lấy
url = 'https://read.qidian.com/chapter/9LjAw1qo2KfhI-Ha6N4TBg2/CCzJu7EvnlnM5j8_3RRvhw2/'

# Gửi yêu cầu GET đến trang web
response = requests.get(url)

# Chuyển đổi nội dung HTML thành đối tượng BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Tìm thẻ div có id="chapter-c" và class="chapter-c" và itemprop="articleBody"
div = soup.find('div', {'class': 'main-text-wrap'})

# Lấy nội dung văn bản bên trong thẻ div
content = div.text.strip()#.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ') => Xóa khoảng tráng thừa

# In nội dung văn bản
print(content)

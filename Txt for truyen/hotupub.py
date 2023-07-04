import requests
from bs4 import BeautifulSoup

# URL của trang web chứa thẻ div cần lấy
url = 'https://www.hotupub.net/book/788/168110.html'

# Gửi yêu cầu GET đến trang web
response = requests.get(url)

# Chuyển đổi nội dung HTML thành đối tượng BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Tìm thẻ div có id="chapter-c" và class="chapter-c" và itemprop="articleBody"
div = soup.find('div', {'class': 'bookread-content-box'})

# Lấy nội dung văn bản bên trong thẻ div
content = div.text.strip()#.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ') => Xóa khoảng tráng thừa

# In nội dung văn bản
print(content)

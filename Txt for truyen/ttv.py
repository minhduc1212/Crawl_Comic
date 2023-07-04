import requests
from bs4 import BeautifulSoup

# URL của trang web chứa thẻ div cần lấy
url = 'https://truyen.tangthuvien.vn/doc-truyen/nhat-nguyet-phong-hoa-reconvert-/chuong-1'

# Gửi yêu cầu GET đến trang web
response = requests.get(url)

# Chuyển đổi nội dung HTML thành đối tượng BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Tìm thẻ div có id="chapter-c" và class="chapter-c" và itemprop="articleBody"
div = soup.find('div', {'class': 'box-chap box-chap-5981336'})

# Lấy nội dung văn bản bên trong thẻ div
content = div.get_text(separator='\n')

# In nội dung văn bản
print(content)
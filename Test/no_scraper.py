import requests
from bs4 import BeautifulSoup

url = "https://i8.xem-truyen.com/831/831983/01-1btm-p2j.jpg?v=1694607129"
headers = {
    'Referer': 'https://blogtruyenmoi.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get(url, headers=headers)
print(response.status_code)
with open('test.jpg', 'wb') as f:
    f.write(response.content)
    f.close()

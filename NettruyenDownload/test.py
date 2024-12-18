import requests
from bs4 import BeautifulSoup

url = "https://nettruyenww.com/truyen-tranh/rainbow/chuong-27/346839"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.nettruyenww.com/'
}
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
with open('test.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())
    f.close()
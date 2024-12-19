import requests
from bs4 import BeautifulSoup

url = "https://nettruyenww.com/truyen-tranh/rainbow-3105"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.nettruyenww.com/'
}
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
ul = soup.find('ul', {'style': 'display: block'})
areas = ul.find_all('div', {'class': 'col-xs-5 chapter'})
for area in areas:
    link = area.find('a')
    with open('link.txt', 'a', encoding='utf-8') as f:
        f.write(link['href'] + '\n')
        f.close()
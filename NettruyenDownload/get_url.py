import requests
from bs4 import BeautifulSoup
import json

url = "https://nettruyenrr.com/Comic/Services/ComicService.asmx/ChapterList?slug=trieu-hoi-den-the-gioi-fantasy&comicId=5998"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.nettruyenrr.com/'
}
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)
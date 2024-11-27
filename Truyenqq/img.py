import requests
from bs4 import BeautifulSoup

url = "https://i125.tintruyen.net/128/1/20.jpg?d=dfgd6546"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Referer": "https://truyenqqviet.com/"
}
response = requests.get(url, headers=headers)
with open("one_piece_chap_1_page_20.jpg", "wb") as file:
    file.write(response.content)
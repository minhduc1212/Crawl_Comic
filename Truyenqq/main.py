import requests
from bs4 import BeautifulSoup

url = "https://truyenqqviet.com/truyen-tranh/one-piece-128-chap-1.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
with open("one_piece_chap_1.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
import requests
from bs4 import BeautifulSoup
from time import sleep

for i in range(1, 310):
    url = f"https://truyenqqviet.com/truyen-moi-cap-nhat/trang-{1}.html"  
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Referer': url
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    areas = soup.find_all('ul', {'class': 'list_grid_out'})
    with open('comic_names_qq.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    comics = areas.find_all('h3')
    with open('comic_names_qq.txt', 'a', encoding='utf-8') as f:
        for comic in comics:
            f.write(comic.text + '\n')
    print(f"Page {i} done")
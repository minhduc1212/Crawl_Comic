from bs4 import BeautifulSoup
import os
import cloudscraper
from urllib.parse import urljoin

url = "https://www.nettruyenplus.com/truyen-tranh/vo-luyen-dinh-phong/chap-1/361803"
scraper = cloudscraper.create_scraper()
info = scraper.get(url) 
 
print(info.status_code)     

soup = BeautifulSoup(info.text, "html.parser") 
body=soup.find('div', {'class':'reading-detail box_doc'})
imgs=body.find_all('img')
print(imgs)
for img in imgs:
    img_link = img['src']
    img_url = urljoin(url, img_link)  # xử lý URL không đầy đủ
    print(img_url)
    filename = img_url.split('/')[-1].split('?')[0]   
    referer = "https://www.nettruyenplus.com/"

    headers =   {
                "Referer": referer
                }
            
    response = scraper.get(img_url, headers=headers)

    with open(filename, 'wb') as f:
        f.write(response.content)
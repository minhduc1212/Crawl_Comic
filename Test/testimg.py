from bs4 import BeautifulSoup
import cloudscraper

scraper = cloudscraper.create_scraper()
response = scraper.get('https://www.nettruyenplus.com/truyen-tranh/vo-luyen-dinh-phong-176960')
soup = BeautifulSoup(response.text, "html.parser") 
areas = soup.find_all('div', {'class': 'col-xs-5 chapter'})

# Tạo danh sách để lưu trữ các đường link đã lấy được và các đường link đã ghi vào file
links = []
written_links = []

# Duyệt qua các phần tử trong danh sách "areas"
for area in areas:
    link = area.find('a')
    chap_link = link['href']
    if chap_link not in links: # Kiểm tra trùng lặp
        links.append(chap_link) # Thêm vào danh sách nếu chưa có
        with open ('E:\LT\Crawl (Python)\Test\links.txt', 'a', encoding='utf-8') as f:
            f.write(str(chap_link) + '\n')
            written_links.append(chap_link) # Thêm vào danh sách các đường link đã ghi vào file

# Đọc lại nội dung của file và lọc các đường link đã được ghi vào file
with open('E:\LT\Crawl (Python)\Test\links.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        if line.strip() not in written_links: # Kiểm tra xem đường link đã được ghi vào file hay chưa
            written_links.append(line.strip())

# Ghi lại các đường link đã lọc vào file
with open('E:\LT\Crawl (Python)\Test\links.txt', 'w', encoding='utf-8') as f:
    for link in written_links:
        f.write(str(link) + '\n')
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from time import sleep

# Khai báo đường dẫn đến trình điều khiển của trình duyệt web
driver_path = "C:/Users/minhd/Downloads/chromedriver_win32/chromedriver.exe"

# Tạo một đối tượng trình duyệt Chrome
driver = webdriver.Chrome(executable_path=driver_path)

# Nhập địa chỉ URL của trang web cần crawl
url = "https://www.hetushu.com/book/203/137625.html"
driver.get(url)

# Lấy mã HTML của trang web đã được thực thi JavaScript
html = driver.page_source

# Sử dụng BeautifulSoup để phân tích cú pháp HTML và trích xuất dữ liệu
soup = BeautifulSoup(html, "html.parser")

# Lưu trữ mã HTML vào tệp hetushu.html
with open("hetushu.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

# Tìm thẻ <link> chứa tệp CSS và lấy URL của tệp này
try:
    css_link = driver.find_element(By.CSS_SELECTOR, "link[href='/command/section.css']")
    css_url = css_link.get_attribute("href")
except:
    print("Không tìm thấy thẻ <link> chứa tệp CSS")
    driver.quit()
    exit()

# Tải tệp CSS và lưu trữ
try:
    driver.get(css_url)
    css_content = driver.page_source
    sleep(5)
    with open("sectioncss.css", "w", encoding="utf-8") as f:
        f.write(str(css_content, "utf-8"))
except:
    print("Không thể tải tệp CSS")
    driver.quit()
    exit()

# Đóng trình duyệt
driver.quit()

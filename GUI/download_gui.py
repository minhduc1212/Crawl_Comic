from tkinter import Tk, Label, Entry, Button, messagebox
from bs4 import BeautifulSoup
import cloudscraper
import os
from time import sleep
from fake_useragent import UserAgent
from urllib.parse import urljoin    
import re
import json
import threading

def download_comic():
    def download_thread():
        url = link_entry.get()
        path = path_entry.get()

        scraper = cloudscraper.create_scraper()
        ua = UserAgent()
        headers = {
            'User-Agent': ua.random,
            'Referer': 'https://www.nettruyenmax.com/'
        }

        response = scraper.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser") 
        
        comic_name = soup.find('h1', {'class':'title-detail'}).text  
        comic_name = re.sub(r'[\/:*?"<>|]', ' ', comic_name)

        sleep(0.5)

        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.exists(os.path.join(path, comic_name)):
            os.makedirs(os.path.join(path, comic_name))

        with open('E:/LT/Crawl (Python)/Data/{}.json'.format(comic_name), 'r', encoding='utf-8') as f:
            data = json.load(f)

        for record in data:
            chap_imgs = record['image_links']
            chap_name = record['chapter_name']
            chap_name = re.sub(r'[\/:*?"<>|]', ' ', chap_name)
            chap_name = " ".join(chap_name.split())

            chap_path = os.path.join(os.path.join(path, comic_name), chap_name)
            if not os.path.exists(chap_path):
                os.makedirs(chap_path)

            img_count = 1
            for img_link in chap_imgs:
                img_link_fix = urljoin(url, img_link)

                response_img = scraper.get(img_link_fix, headers=headers)

                filename = f'{img_count:03}.jpg'

                with open(os.path.join(chap_path, filename), 'wb') as f:
                    f.write(response_img.content)
                img_count += 1
            message_label.config(text="Đã tải xong " + chap_name) 
            sleep(0.5)

        messagebox.showinfo("Download Complete", "Comic downloaded successfully!")

    # Create a new thread for downloading
    download_thread = threading.Thread(target=download_thread)
    download_thread.start()

# Create main window
window = Tk()
window.title("Comic Downloader")

# Create labels
link_label = Label(window, text="Link Truyện:")
link_label.pack()
link_entry = Entry(window)
link_entry.pack()

path_label = Label(window, text="Vị Trí Tải Truyện:")
path_label.pack()   
path_entry = Entry(window)
path_entry.pack()

# Create download button
download_button = Button(window, text="Download", command=download_comic)
download_button.pack()

message_label = Label(window, text="")
message_label.pack()

# Start the main event loop
window.mainloop()
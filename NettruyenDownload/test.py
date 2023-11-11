import threading
import os
import re
from urllib.parse import urljoin
from tkinter import Tk, Label, Entry, Button, messagebox
from tkinter.ttk import Progressbar
import cloudscraper
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def download_comic(url, path):
    def get_data(areas):
        data = []
        message_label.config(text="Đang lấy data...")
        for area in areas:
            link = area.find('a')
            chap_name = area.get_text().strip()
            chap_name = re.sub(r'[\\/:*?"<>|]', ' ', chap_name)
            chap_names = []
            chap_names.append(chap_name)

            data_one = {
                "chapter_name": chap_name,
                "image_links": []
            }

            chap_links = []
            chap_links.append(link['href'])
            for chap_link in chap_links:
                chap_response = scraper.get(chap_link, headers=headers)
                chap_soup = BeautifulSoup(chap_response.text, "html.parser")
                chap_imgs_div = chap_soup.find('div', {'class': 'reading-detail box_doc'})
                chap_imgs = chap_imgs_div.find_all('img')

                data_one["image_links"].extend([img.get('src') for img in chap_imgs])
            data.append(data_one)
        return data
    
    def progress_start(total_chapters):
        progress_bar.config(maximum=total_chapters, value=0)
        message_label.config(text="Đang tải...")

    def progress_end(index, chap_name):
        progress_bar.config(value=index)
        message_label.config(text="Đã tải xong " + chap_name)

    def download_chapter(chap_imgs, chap_path):
         for img_count, img_link in enumerate(chap_imgs, start=1):
            img_link_fix = urljoin(url, img_link)
            response_img = scraper.get(img_link_fix, headers=headers)
            filename = f'{img_count:03}.jpg'

            with open(os.path.join(chap_path, filename), 'wb') as f:
                f.write(response_img.content)
                f.close()

    def download_comic(data, comic_name):
        total_chapters = len(data)

        thread1 = threading.Thread(target=progress_start, args=(total_chapters,))
        thread1.start()

        for index, record in enumerate(data, start=1):
            chap_imgs = record['image_links']
            chap_name = record['chapter_name']
            chap_name = re.sub(r'[\/:*?"<>|]', ' ', chap_name)
            chap_name = " ".join(chap_name.split())

            chap_path = os.path.join(os.path.join(path, comic_name), chap_name)
            if not os.path.exists(chap_path):
                os.makedirs(chap_path)

            download_chapter(chap_imgs, chap_path)
         
            thread3 = threading.Thread(target=progress_end, args=(index, chap_name))
            thread3.start()
            
        messagebox.showinfo("Download Complete", "Comic downloaded successfully!")

    if not os.path.exists(path):
        os.makedirs(path)

    scraper = cloudscraper.create_scraper()
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Referer': 'https://www.nettruyenus.com/'
    }

    response = scraper.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    comic_name = soup.find('h1', {'class': 'title-detail'}).text
    comic_name = re.sub(r'[\\/:*?"<>|]', ' ', comic_name)

    if not os.path.exists(os.path.join(path, comic_name)):
        os.makedirs(os.path.join(path, comic_name))

    areas = soup.find_all('div', {'class': 'col-xs-5 chapter'})
    data = get_data(areas)
    download_comic(data, comic_name)

def start_download():
    url = link_entry.get()
    path = path_entry.get()
    thread=threading.Thread(target=download_comic, args=(url, path))
    thread.start()

window = Tk()
window.title("Comic Downloader")

link_label = Label(window, text="Link Truyện:")
link_label.pack()
link_entry = Entry(window)
link_entry.pack()

path_label = Label(window, text="Vị Trí Tải Truyện:")
path_label.pack()
path_entry = Entry(window)
path_entry.pack()

download_button = Button(window, text="Download", command=start_download)
download_button.pack()

progress_bar = Progressbar(window, mode="determinate")
progress_bar.pack()

message_label = Label(window, text="")
message_label.pack()

window.mainloop()
path = path_entry.get()
threading.Thread(target=download_comic).start()

window = Tk()
window.title("Comic Downloader")

link_label = Label(window, text="Link Truyện:")
link_label.pack()
link_entry = Entry(window)
link_entry.pack()

path_label = Label(window, text="Vị Trí Tải Truyện:")
path_label.pack()
path_entry = Entry(window)
path_entry.pack()

download_button = Button(window, text="Download", command=download_comic)
download_button.pack()

progress_bar = Progressbar(window, mode="determinate")
progress_bar.pack()

message_label = Label(window, text="")
message_label.pack()

window.mainloop()
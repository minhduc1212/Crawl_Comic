import threading
import os
import re
from urllib.parse import urljoin
from tkinter import Tk, Label, Entry, Button, messagebox, filedialog
from tkinter.ttk import Progressbar
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from time import sleep


def download_comic_total(url, path):
    data = []  
    def get_data(areas):
        error=False
        error_chapter = []
        message_label.config(text="Đang lấy data...")
        for area in areas:
            link = area.find('a')
            chap_name = area.get_text().strip()
            chap_name = re.sub(r'[\\/:*?"<>|.]', ' ', chap_name)
            chap_names = []
            chap_names.append(chap_name)

            data_one = {
                "chapter_name": chap_name,
                "image_links": []
            }

            chap_links = []
            chap_links.append(link['href'])
            for chap_link in chap_links:
                chap_response = requests.get(chap_link, headers=headers)
                chap_soup = BeautifulSoup(chap_response.text, "html.parser")
                chap_imgs_div = chap_soup.find('div', {'class': 'reading-detail box_doc'})
                try:
                    chap_imgs = chap_imgs_div.find_all('img')
                except:
                    try:
                        sleep(1)
                        chap_response = requests.get(chap_link, headers=headers)
                        chap_soup = BeautifulSoup(chap_response.text, "html.parser")
                        chap_imgs = chap_soup.find_all('img')
                        continue
                    except:
                        error_chapter.append(data_one)
                        error = True
                        print('Error', chap_link)
                        continue

                for img in chap_imgs:
                    if 'data-src' in img.attrs:
                        data_one["image_links"].append(img['data-src'])
            data.append(data_one)
        return data, error_chapter, error
    
    def progress_start(total_chapters):
        progress_bar.config(maximum=total_chapters, value=0)
        message_label.config(text="Đang tải...")

    def progress_end(index, chap_name):
        progress_bar.config(value=index)
        message_label.config(text="Đã tải xong " + chap_name)

    def download_chapter(chap_imgs, chap_path):
         for img_count, img_link in enumerate(chap_imgs, start=1):
            img_link_fix = urljoin(url, img_link)
            response_img = requests.get(img_link_fix, headers=headers)
            filename = f'{img_count:03}.jpg'
            with open(os.path.join(chap_path, filename), 'wb') as f:
                f.write(response_img.content)
                f.close()

    def download_comic(data, comic_name):
        total_chapters = len(data)
        progress_start(total_chapters)

        for index, record in enumerate(data, start=1):
            chap_imgs = record['image_links']
            chap_name = record['chapter_name']
            chap_name = re.sub(r'[\/:*?"<>|]', ' ', chap_name)
            chap_name = " ".join(chap_name.split())

            chap_path = os.path.join(os.path.join(path, comic_name), chap_name)
            if not os.path.exists(chap_path):
                os.makedirs(chap_path)

            download_chapter(chap_imgs, chap_path)
         
            progress_end(index, chap_name)
            
        messagebox.showinfo("Download Complete", "Comic downloaded successfully!")

    if not os.path.exists(path):
        os.makedirs(path)
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Referer': 'https://www.nettruyenrr.com/'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    comic_name = soup.find('h1', {'class': 'title-detail'}).text
    comic_name = re.sub(r'[\\/:*?"<>|]', ' ', comic_name)

    if not os.path.exists(os.path.join(path, comic_name)):
        os.makedirs(os.path.join(path, comic_name))

    ul = soup.find('ul', {'id': 'chapter_list'})
    areas = ul.find_all('div', {'class': 'col-xs-5 chapter'})
    data, error_chapter, error = get_data(areas)
    download_comic(data, comic_name)
    if error:
        download_comic(error_chapter, comic_name)
        
    
def select_path():
    path = filedialog.askdirectory()
    path_entry.delete(0, 'end')
    path_entry.insert(0, path)
    return path

def start_download():
    url = link_entry.get()
    path = path_entry.get()
    thread=threading.Thread(target=download_comic_total, args=(url, path))
    thread.start() 
    
# Tạo cửa sổ
window = Tk()
window.title("Nettruyen Downloader")

# Label và Entry cho link truyện
link_label = Label(window, text="Link Truyện:")
link_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
link_entry = Entry(window, width=40)
link_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

# Label và Entry cho vị trí tải truyện
path_label = Label(window, text="Vị Trí Tải Truyện:")
path_label.grid(row=1, column=0, sticky='w', padx=10, pady=5)
path_entry = Entry(window, width=40)
path_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

# Nút Download
download_button = Button(window, text="Download", command=start_download)
download_button.grid(row=2, column=0, columnspan=3, pady=10)

# Button để chọn đường dẫn
path_button = Button(window, text="Browse", command=select_path)
path_button.grid(row=1, column=3, padx=10, pady=5)

# Progress bar
progress_bar = Progressbar(window, mode="determinate")
progress_bar.grid(row=3, column=0, columnspan=3, pady=5)

# Label thông báo
message_label = Label(window, text="", wraplength=400)
message_label.grid(row=4, column=0, columnspan=3, pady=10)

# Mở cửa sổ
window.mainloop()
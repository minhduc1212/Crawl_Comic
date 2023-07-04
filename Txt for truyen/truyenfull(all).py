import os
import requests
from bs4 import BeautifulSoup

# URL của trang web
url = "https://truyenfull.vn/linh-vu-thien-ha/chuong-{}/"

# Tạo thư mục để lưu các file HTML
if not os.path.exists("1"):
    os.makedirs("1")

# Số lần lặp để crawl dữ liệu cho các trang tiếp theo
num_of_pages = 10

# Vòng lặp để crawl dữ liệu cho các trang tiếp theo
for i in range(1, num_of_pages+1):
    # Tạo đường dẫn của trang tiếp theo
    next_url = url.format(i)
    
    # Gửi yêu cầu GET đến đường dẫn của trang tiếp theo
    response = requests.get(next_url)
    
    # Kiểm tra mã trạng thái của phản hồi
    if response.status_code == 200:
        # Nếu thành công, sử dụng thư viện BeautifulSoup để phân tích cú pháp HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Lưu dữ liệu vào file HTML trong thư mục "1"
        file_name = os.path.join("1", f"{i}.txt")

        text = soup.get_text()
        cleaned_text=text.replace('Hiện menudoc truyen Danh sách Truyện mới cập nhậtTruyện HotTruyện FullTiên Hiệp HayKiếm Hiệp HayTruyện Teen HayNgôn Tình HayNgôn Tình SắcNgôn Tình NgượcNgôn Tình SủngNgôn Tình HàiĐam Mỹ HàiĐam Mỹ HayĐam Mỹ H VănĐam Mỹ Sắc Thể loại  Tiên HiệpKiếm HiệpNgôn TìnhĐam MỹQuan TrườngVõng DuKhoa HuyễnHệ ThốngHuyền HuyễnDị GiớiDị NăngQuân SựLịch SửXuyên KhôngXuyên NhanhTrọng SinhTrinh ThámThám HiểmLinh DịNgượcSủngCung ĐấuNữ CườngGia ĐấuĐông PhươngĐô ThịBách HợpHài HướcĐiền VănCổ ĐạiMạt ThếTruyện TeenPhương TâyNữ PhụLight NovelViệt NamĐoản VănKhác   Phân loại theo Chương   Dưới 100 chương 100 - 500 chương 500 - 1000 chương Trên 1000 chương  Truyện Tranh Tùy chỉnh  Màu nềnXám nhạtXanh nhạtVàng nhạtMàu sepiaXanh đậmVàng đậmVàng ốMàu trắngHạt sạnSách cũMàu tốiFont chữPalatino LinotypeBookerlyMinionSegoe UIRobotoRoboto CondensedPatrick HandNoticia TextTimes New RomanVerdanaTahomaArialSize chữ16182022242628303234363840Chiều cao dòng100%120%140%160%180%200%Full khung Có Không', '')

        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)
        # Xử lý dữ liệu ở đây
        print(f"Crawled data from page {i}")
    else:
        # Nếu không thành công, hiển thị thông báo lỗi
        print(f"Failed to crawl data from page {i}")
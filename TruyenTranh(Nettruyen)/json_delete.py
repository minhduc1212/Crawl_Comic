import os

# Đường dẫn tới thư mục chứa các tệp tin
directory = 'E:/LT/Crawl (Python)/Data'

# Liệt kê các tệp tin trong thư mục
for filename in os.listdir(directory):
    if "_list" in filename:  # Kiểm tra xem "_list" có xuất hiện trong tên tệp tin hay không
        file_path = os.path.join(directory, filename)
        os.remove(file_path)
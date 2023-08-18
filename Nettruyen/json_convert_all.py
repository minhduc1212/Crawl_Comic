import os
import json

def get_file_names(directory):
    file_names = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_names.append(filename)
    return file_names

# Đường dẫn tới thư mục cần lấy tên file
directory = 'E:/LT/Crawl (Python)/Data'

new_directory='E:/LT/Crawl (Python)/Data_list'

# Gọi hàm để lấy danh sách tên file
file_names = get_file_names(directory)

for file_name in file_names:
    if file_name.endswith('.json'):  # Chỉ xử lý các tệp tin có phần mở rộng .json
        file_path = os.path.join(directory, file_name)
        data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                data_one = json.loads(line)
                data.append(data_one)
        
        new_file_path = os.path.join(new_directory, file_name)
        with open(new_file_path, 'w', encoding='utf-8') as s:
            json.dump(data, s, ensure_ascii=False)
    print('Xong ', file_name)
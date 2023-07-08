import json

data = []

with open('Ngày tôi sinh ra, bách quỷ dạ hành, tuyết thi hộ đạo.json', 'r', encoding='utf-8') as f:
    for line in f:
        data_one = json.loads(line)
        data.append(data_one)

with open('Ngày tôi sinh ra, bách quỷ dạ hành, tuyết thi hộ đạo_list.json', 'w', encoding='utf-8') as s:
    json.dump(data,s)
import json

data = []

with open('Kingdom - Vương Giả Thiên Hạ.json', 'r', encoding='utf-8') as f:
    for line in f:
        data_one = json.loads(line)
        data.append(data_one)

with open('Kingdom - Vương Giả Thiên Hạ_list.json', 'w', encoding='utf-8') as s:
    json.dump(data,s)
import json

data = []

with open('all_comics_links.json', 'r', encoding='utf-8') as f:
    for line in f:
        data_one = json.loads(line)
        data.append(data_one)

with open('all_comics_links_list.json', 'w', encoding='utf-8') as s:
    json.dump(data,s, ensure_ascii=False)
import json

data = []

with open('Tu La Võ Thần.json', 'r', encoding='utf-8') as f:
    for line in f:
        data_one = json.loads(line)
        data.append(data_one)

with open('Tu La Võ Thần.json', 'w', encoding='utf-8') as s:
    json.dump(data,s, ensure_ascii=False)
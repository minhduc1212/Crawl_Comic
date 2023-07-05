import json

with open('Yumin ni Gomeshi o Tabe Sasetai.json', 'r') as f:
    data = json.load(f)

for record in data:
    name = record['chapter_name']
    chap_imgs = record['image_links']
    chap_imgs_str = ', '.join(chap_imgs)
    print(chap_imgs_str)
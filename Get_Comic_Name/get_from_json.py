import json
comics = ''
with open ('all_comics_links_list.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for comic in data:
        comics += comic['comic_name'] + '\n'
with open('comic_names_qq.json', 'w', encoding='utf-8') as f:
    f.write(comics)
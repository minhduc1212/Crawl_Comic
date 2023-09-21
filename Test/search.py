from unidecode import unidecode

def remove_accents(text):
    return unidecode(text)

def search_words(word_list, search_term):
    matching_words = []
    for word in word_list:
        if remove_accents(search_term.lower()) in remove_accents(word.lower()):
            matching_words.append(word)
    return matching_words

import json

with open('all_comics_links_list.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
comic_names=[]
for item in data:
    comic_name=item['comic_name']
    comic_names.append(comic_name)
    
search_term = 'O re'

matching_results = search_words(comic_names, search_term)

print("Kết quả tìm kiếm:")
for word in matching_results:
    print(word)
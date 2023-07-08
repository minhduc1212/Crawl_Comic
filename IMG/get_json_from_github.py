import requests
import json

response=requests.get('https://raw.githubusercontent.com/minhduc1212/Crawl_Comic/master/Th%E1%BA%A7n%20Binh%20Phong%20Th%E1%BA%A7n.json')
data = json.loads(response.text)
with open('2.json', 'w', encoding='utf-8') as f:
    f.write(str(data))

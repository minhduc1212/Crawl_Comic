import requests

url = "https://cdnntx.com/nettruyen/cbunu-triangle-and-circle/3/2.jpg"
headers = {
    'Referer': 'https://nettruyenxx.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get(url, headers=headers)
print(response.status_code)
with open('test.jpg', 'wb') as f:
    f.write(response.content)
    f.close()

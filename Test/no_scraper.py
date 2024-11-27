import requests

url = "https://s3.mideman.com/file/mideman/cmanga/chapter/518696/0.png?v=2"
headers = {
    'Referer': 'https://nettruyendie.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get(url, headers=headers)
print(response.status_code)
with open('test.jpg', 'wb') as f:
    f.write(response.content)
    f.close()

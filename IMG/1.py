import requests
from bs4 import BeautifulSoup

post_body = {
  "cmd": "request.get",
  "url":"https://www.nettruyenplus.com/truyen-tranh/vo-luyen-dinh-phong/chap-1/36180",
  "maxTimeout": 60000
}

response = requests.post('http://localhost:8191/v1', headers={'Content-Type': 'application/json'}, json=post_body)

if response.status_code == 200:
    json_response = response.json()
    if json_response.get('status') == 'ok':

        ## Get Cookies & Clean
        cookies = json_response['solution']['cookies']
        clean_cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}

        ## Print Cookies
        print("Cookies:")
        for cookie in cookies:
            print(cookie['name'], ":", cookie['value'])

        ## Get User-Agent
        user_agent = json_response['solution']['userAgent']

        ## Make normal request
        headers={"User-Agent": user_agent}

        response = requests.get("https://www.nettruyenplus.com/truyen-tranh/vo-luyen-dinh-phong/chap-1/36180", headers=headers, cookies=clean_cookies_dict)
        if response.status_code == 200:
            ## ...parse data from response
            print('Success')
        if response.status_code == 200:
            ## Parse HTML content using Beautiful Soup
            soup = BeautifulSoup(response.content, 'html.parser')
            soup_str=str(soup)
            with open('1.txt', 'w', encoding="utf-8") as a:
              a.write(soup_str)
            
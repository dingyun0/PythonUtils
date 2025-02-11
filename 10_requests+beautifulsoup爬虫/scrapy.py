import requests
from bs4 import BeautifulSoup4

url="https://www.baidu.com"

response=requests.get(url)
soup=BeautifulSoup4(response.text,"html.parser")
title=soup.title.string
print(title)
print("页面连接")
for link in soup.find_all("a"):
    href=link.get("href")
    if href:
        response=requests.get(href)

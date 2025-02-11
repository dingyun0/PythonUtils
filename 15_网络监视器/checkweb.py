import requests
import time

def check_website(url):
    try:
        response=requests.get(url,timeout=10)
        return response.status_code==200
    except:
        return False

website_url="https://www.baidu.com"
check_interval=5
max_retries=3

print(f"开始监控{website_url}")
retry_count=0
while True:
    if check_website(website_url):
        print(f"{website_url}正常访问")
        retry_count=0
    else:
        retry_count+=1
        if retry_count>=max_retries:
            print(f"{website_url}无法访问，已达到最大重试次数")
            break
    time.sleep(check_interval)


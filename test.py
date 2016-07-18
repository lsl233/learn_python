# coding: utf8
import urllib.request
from bs4 import BeautifulSoup


url = 'http://baike.baidu.com/link?url=fmmXvjzLfsWot1X9sIvnbeHw4Wt2rfzRfK3fPWvNVpWtxK6SK0ZEcDQrGh2ktW8iuVOXsrlYxkyOBQkrmBKyPq'
response = urllib.request.urlopen(url)
data = response.read()

soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
print(soup.prettify())
print('获取所有链接')
links = soup.find_all('a')
for a in links:
    print(a.name, a['href'], a.get_text)

from bs4 import BeautifulSoup
import requests

# baidu=requests.get('http://www.baidu.com')
# print(baidu) #<Response [200]>意味着网页请求成功

baidu=requests.get('http://www.baidu.com').content #抓取网页content

soup=BeautifulSoup(baidu,'html.parser')
# print(soup.text)

links=soup.findAll('a')
print(links)
print('--------------------')

for link in links:
    print(link.string)


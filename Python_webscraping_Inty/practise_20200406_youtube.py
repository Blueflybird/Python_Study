from bs4 import BeautifulSoup
import requests


data=requests.get('http://www.google.com').content #抓取网页content

soup=BeautifulSoup(data,'html.parser')

# print(soup.title.text)
print(soup.body.div.attrs)

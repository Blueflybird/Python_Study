from bs4 import BeautifulSoup

myHtml='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>this is title from inty</title>
</head>
<body>
<h1>This is H1</h1>
<h1>这是另外一个H1</h1>
<h2>this is h2, 小一点的字体</h2>
<p> this is inty, i love you guys. yes!!!</p>
</body>
</html>'''

soup=BeautifulSoup(myHtml,'html.parser')
myH1=soup.find('h1')
print(myH1.string)
myH2=soup.find('h2')
print(myH2.string)

print('---------------')
myH1=soup.findAll('h1') #抓取所有的h1

for i in myH1:
    if '这是' in i.string: #加个逻辑
        print(i.string)
